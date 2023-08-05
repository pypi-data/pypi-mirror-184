import yaml
from traitlets import Bool, Dict, Int, List, Unicode
from traitlets.config.configurable import Configurable


# TODO: Change to custom TraitTypes from validation.common in dictionaries
class PipelineConfiguration(Configurable):
    sources = List(
        trait=Dict(
            per_key_traits={
                "pipeline_name": Unicode(allow_none=False),
                "from": Unicode(allow_none=False),
                "type": Unicode(allow_none=False),
                "into": Unicode(allow_none=False),
                "params": Unicode(allow_none=True),
            }
        ),
        allow_none=True,
    ).tag(config=True)

    transformations = List(
        trait=Dict(
            per_key_traits={
                "pipeline_name": Unicode(allow_none=False),
                "from": Unicode(allow_none=False),
                "into": Unicode(allow_none=False),
                "column_order": Int(allow_none=True),
                "source_column_name": Unicode(allow_none=True),
                "source_column_type": Unicode(allow_none=True),
                "dest_column_name": Unicode(allow_none=True),
                "dest_column_type": Unicode(allow_none=True),
                "transform_function": Unicode(allow_none=True),
                "sql_query": Unicode(allow_none=True),
                "default_value": Unicode(allow_none=True),
                "not_null": Bool(allow_none=True),
            }
        ),
        allow_none=True,
    ).tag(config=True)

    destinations = List(
        trait=Dict(
            per_key_traits={
                "pipeline_name": Unicode(allow_none=False),
                "from": Unicode(allow_none=False),
                "into": Unicode(allow_none=False),
                "path": Unicode(allow_none=True),
                "keys": List(trait=Unicode(allow_none=False), allow_none=False),
                "partition_by": List(trait=Unicode(allow_none=False), allow_none=True),
                "sequence_by": Unicode(allow_none=False),
            }
        ),
        allow_none=True,
    ).tag(config=True)

    def __str__(self):
        str_repr = {
            "sources": self.sources,
            "transformations": self.transformations,
            "destinations": self.destinations,
        }

        return yaml.dump(str_repr, allow_unicode=True, default_flow_style=False)

    def to_dict(self):
        return {
            "sources": self.sources,
            "transformations": self.transformations,
            "destinations": self.destinations,
        }
