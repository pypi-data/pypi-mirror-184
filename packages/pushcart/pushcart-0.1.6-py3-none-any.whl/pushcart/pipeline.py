if __package__:
    from pushcart import dbutils

import os
from pathlib import Path

from traitlets import Unicode
from traitlets.config import Application

from pushcart.configuration import PipelineConfiguration


class Pipeline(Application):
    classes = [PipelineConfiguration]
    config_file = Unicode(
        default_value="pipeline_run", help="pipeline configuration file base name"
    ).tag(config=True)

    aliases = {
        "pipeline_name": "Configuration.pipeline_name",
        "sources": "Configuration.sources",
        "transformations": "Configuration.transformations",
        "destinations": "Configuration.destinations",
        ("c", "config-file"): "Pipeline.config_file",
    }

    def initialize(self, argv=None):
        super().initialize(argv=argv)

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

        if self.config_file:
            self.load_config_file(
                self.config_file, [os.path.join(cwd, "configuration")]
            )

    def start(self):
        print(Configuration(parent=self))

    @classmethod
    def get_subapp_instance(cls, app: Application) -> Application:
        app.clear_instance()  # since Application is singleton, need to clear main app
        return cls.instance(parent=app)
