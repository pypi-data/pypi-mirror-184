if __package__:
    from pushcart import dbutils, spark

import os
from logging import ERROR, INFO
from pathlib import Path

from databricks_cli.clusters.api import ClusterApi
from databricks_cli.configure.config import _get_api_client
from databricks_cli.configure.provider import DatabricksConfig
from databricks_cli.pipelines.api import PipelinesApi
from traitlets import Bool, Unicode
from traitlets.config import Application

from pushcart.configuration import PipelineConfiguration


class Release(Application):
    classes = [PipelineConfiguration]
    config_file = Unicode(
        default_value="release", help="release configuration file base name"
    ).tag(config=True)

    host = Unicode(allow_none=True, help="URL of Databricks instance")
    token = Unicode(allow_none=True, help="User token to log into Databricks")
    user = Unicode(allow_none=False, help="Databricks Repos user where repo is cloned")
    repo = Unicode(allow_none=False, help="Name of Git repository for DLT pipelines")
    non_destructive = Bool(
        default_value=False,
        allow_none=True,
        help="Remove or ignore obsolete DLT pipelines",
    )

    aliases = {
        "sources": "PipelineConfiguration.sources",
        "transformations": "PipelineConfiguration.transformations",
        "destinations": "PipelineConfiguration.destinations",
        ("c", "config-file"): "Release.config_file",
        "log-level": "Release.log_level",
        "host": "Release.host",
        "token": "Release.token",
        "user": "Release.user",
        "repo": "Release.repo",
        ("nd", "non-destructive"): "Release.non_destructive",
    }

    flags = {
        "info": ({"Release": {"log_level": INFO}}, "Set log level to INFO"),
        "error": ({"Release": {"log_level": ERROR}}, "Set log level to ERROR"),
        "true": (
            {"Release": {"non_destructive": True}},
            "Ignore obsolete DLT pipelines",
        ),
        "false": (
            {"Release": {"non_destructive": False}},
            "Remove obsolete DLT pipelines",
        ),
    }

    @classmethod
    def get_subapp_instance(cls, app: Application) -> Application:
        """
        Needs to run if the release is a subapp, or if in the presence of the
        IPython Kernel (i.e. from Databricks). Since Application is a singleton,
        we need to clear main app
        """
        app.clear_instance()
        return cls.instance(parent=app)

    def initialize(self, argv=None):
        super().initialize(argv=argv)

        self.log_format = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
        self.log_datefmt = "%Y-%m-%dT%H:%M:%S%z"

        if __package__:
            cwd = Path(__file__).parent
        else:
            notebook_path = (
                dbutils.notebook.entry_point.getDbutils()
                .notebook()
                .getContext()
                .notebookPath()
                .get()
            )
            cwd = os.path.join(
                "/Workspace",
                os.path.dirname(os.path.abspath(notebook_path)).lstrip("/"),
            )

        self.log.info(f"Running release from {cwd}")

        if self.repo:
            spark.conf.set("pushcart.repo_name", self.repo)

        if self.user:
            spark.conf.set("pushcart.repo_user", self.user)

        if self.config_file:
            self.load_config_file(
                self.config_file, [os.path.join(cwd, "configuration", "presets")]
            )

    def start(self):
        self.__create_backend_objects()

        client = self.__get_api_client(self.host, self.token)

        workspace_pipelines = self.get_workspace_pipelines_list()
        scheduled_pipelines = self.get_scheduled_pipelines_list(client)
        new_pipelines = self.get_new_pipelines_list(
            workspace_pipelines, scheduled_pipelines
        )
        self.create_new_pipelines(client, new_pipelines)

        obsolete_pipelines = self.get_obsolete_pipelines_list(
            workspace_pipelines, scheduled_pipelines
        )

        if self.non_destructive:
            if obsolete_pipelines:
                self.log.warning(
                    f"Release run in non-destructive mode. Obsolete DLT pipelines ignored:"
                )
                for p in obsolete_pipelines:
                    self.log.warning(f"- {p}")

            return

        self.delete_obsolete_pipelines(client, obsolete_pipelines)

    def __create_backend_objects(self):
        schemas = {
            "sources": "struct<pipeline_name:string,from:string,type:string,into:string,params:string>",
            "transformations": "struct<pipeline_name:string,from:string,into:string,column_order:int,source_column_name:string,source_column_type:string,dest_column_name:string,dest_column_type:string,transform_function:string,sql_query:string,default_value:string,not_null:boolean>",
            "destinations": "struct<pipeline_name:string,from:string,into:string,path:string,keys:array<string>,partition_cols:array<string>,sequence_by:string>",
        }

        spark.sql("CREATE DATABASE IF NOT EXISTS metadata")

        for stage_name, schema in schemas.items():
            stage_df = spark.createDataFrame(
                self.config.PipelineConfiguration[stage_name], schema=schema
            )
            stage_df.write.saveAsTable(
                f"metadata.{stage_name}", format="delta", mode="overwrite"
            )

            self.log.info(f"Wrote {stage_name} metadata table.")

    @staticmethod
    def __get_api_client(host: str, token: str) -> DatabricksConfig:
        config = DatabricksConfig.from_token(host, token, False)

        return _get_api_client(config)

    @staticmethod
    def __get_api_node_types(client: DatabricksConfig) -> list:
        ca = ClusterApi(client)

        return ca.list_node_types().get("node_types", [])

    @staticmethod
    def __get_api_pipeline_list(client: DatabricksConfig) -> list:
        pa = PipelinesApi(client)

        return pa.list()

    def __delete_pipeline(self, client: DatabricksConfig, pipeline_id: str) -> None:
        pa = PipelinesApi(client)
        pa.delete(pipeline_id)

        self.log.info(f"Deleted {pipeline_id}")

    def __create_pipeline(self, client: DatabricksConfig, settings: dict) -> str:
        pa = PipelinesApi(client)
        pipeline = pa.create(settings, os.path.curdir, allow_duplicate_names=False)

        self.log.info(
            f"Created pipeline: {settings['name']} ({pipeline['pipeline_id']})"
        )
        return pipeline["pipeline_id"]

    def get_workspace_pipelines_list(self) -> list:
        src_df = spark.table("metadata.sources").select("pipeline_name")
        transf_df = spark.table("metadata.transformations").select("pipeline_name")
        dest_df = spark.table("metadata.destinations").select("pipeline_name")

        pipelines_df = src_df.union(transf_df).union(dest_df).distinct()
        workspace_pipelines = pipelines_df.pandas_api().get("pipeline_name").tolist()

        self.log.debug("Found workspace pipelines:")
        for p in workspace_pipelines:
            self.log.debug(f"- {p}")

        if not workspace_pipelines:
            self.log.debug("- None")

        return workspace_pipelines

    def get_scheduled_pipelines_list(self, client: DatabricksConfig) -> list:
        api_pipelines = self.__get_api_pipeline_list(client)

        pipelines = []
        self.log.debug("Found scheduled pipelines:")
        for p in api_pipelines:
            pipelines.append({p["pipeline_id"]: p["name"]})
            self.log.debug(f"- {p['name']} ({p['pipeline_id']})")

        if not pipelines:
            self.log.debug("- None")

        return pipelines

    def get_obsolete_pipelines_list(
        self, workspace_pipelines: list, scheduled_pipelines: list
    ) -> list:
        obsolete_pipelines = set()

        self.log.debug("Found obsolete pipelines:")
        for p in scheduled_pipelines:
            for p_id, p_name in p.items():
                if p_name not in workspace_pipelines:
                    obsolete_pipelines.add(p_id)
                    self.log.debug(f"- {p_name} ({p_id})")

        if not obsolete_pipelines:
            self.log.debug("- None")

        return obsolete_pipelines

    def delete_obsolete_pipelines(
        self, client: DatabricksConfig, obsolete_pipelines: list
    ) -> None:
        self.log.info("Deleting DLT pipelines for data flows that no longer exist")
        for p in obsolete_pipelines:
            self.__delete_pipeline(client, p)

    def get_new_pipelines_list(
        self, workspace_pipelines: list, scheduled_pipelines: list
    ) -> list:
        for p in scheduled_pipelines:
            for p_id, p_name in p.items():
                if p_name in workspace_pipelines:
                    workspace_pipelines.remove(p_name)

        self.log.debug("Found new pipelines:")
        if not workspace_pipelines:
            self.log.debug("- None")
        else:
            for p in workspace_pipelines:
                self.log.debug("- ", p)

        return workspace_pipelines

    def get_node_types_list(self, client: DatabricksConfig):
        api_node_types = self.__get_api_node_types(client)

        sorted_node_types = sorted(
            api_node_types, key=lambda k: (k["num_cores"], k["memory_mb"])
        )

        node_types = [
            t["node_type_id"]
            for t in sorted_node_types
            if (not t["is_deprecated"]) and ("deprecated" not in t["description"])
        ]
        return node_types

    def __get_cluster_config_for_pipeline(self, pipeline_name: str) -> list:
        for cluster_config in self.config.PipelineConfiguration["clusters"]:
            if matched_config := cluster_config.get(pipeline_name):
                return matched_config

    def create_new_pipelines(
        self, client: DatabricksConfig, new_pipeline_names: list
    ) -> None:
        new_pipelines = []

        self.log.info("Scheduling new pipelines")

        # New pipeline: https://docs.databricks.com/workflows/delta-live-tables/delta-live-tables-api-guide.html#pipeline-spec

        for p in new_pipeline_names:
            cluster_settings = self.__get_cluster_config_for_pipeline(p)

            if not cluster_settings:
                cluster_settings = [{"label": "default", "num_workers": 2}]

            settings = {
                "name": p,
                "storage": None,  # Set per DLT table
                "target": p,
                "clusters": cluster_settings,
                "libraries": [
                    {
                        "notebook": {
                            "path": f"/Repos/{self.user}/{self.repo}/runner/pipeline"
                        }
                    }
                ],
            }

            pipeline_id = self.__create_pipeline(client, settings)
            new_pipelines.append(pipeline_id)

        return new_pipelines


if __name__ == "__main__":
    if app := Application.instance():
        r = Release.get_subapp_instance(app=app)
    else:
        r = Release.instance()

    r.launch_instance()
