if __package__:
    from pushcart import dbutils, spark

import os
from logging import ERROR, INFO
from pathlib import Path

from traitlets import Unicode
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
    }

    flags = {
        "info": ({"Release": {"log_level": INFO}}, "Set log level to INFO"),
        "error": ({"Release": {"log_level": ERROR}}, "Set log level to ERROR"),
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


if __name__ == "__main__":
    if app := Application.instance():
        r = Release.get_subapp_instance(app=app)
    else:
        r = Release.instance()

    r.launch_instance()
