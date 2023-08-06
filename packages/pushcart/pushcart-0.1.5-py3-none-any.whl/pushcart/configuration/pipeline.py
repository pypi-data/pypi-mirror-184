import yaml
from traitlets import Bool, Dict, Int, List, Unicode
from traitlets.config.configurable import Configurable


# TODO: Change to custom TraitTypes from validation.common in dictionaries
class PipelineConfiguration(Configurable):
    # Cluster settings https://docs.databricks.com/workflows/delta-live-tables/delta-live-tables-api-guide.html#pipelinesnewcluster
    clusters = List(
        Dict(
            value_trait=List(
                Dict(
                    per_key_traits={
                        "label": Unicode(default_value="default", allow_none=True),
                        "spark_conf": Dict(allow_none=True),
                        "aws_attributes": Dict(allow_none=True),
                        "node_type_id": Unicode(allow_none=True),
                        "driver_node_type_id": Unicode(allow_none=True),
                        "ssh_public_keys": List(
                            trait=Unicode(allow_none=False), allow_none=True
                        ),
                        "custom_tags": Dict(allow_none=True),
                        "cluster_log_conf": Dict(allow_none=True),
                        "spark_env_vars": Dict(allow_none=True),
                        "init_scripts": Dict(allow_none=True),
                        "instance_pool_id": Unicode(allow_none=True),
                        "driver_instance_pool_id": Unicode(allow_none=True),
                        "policy_id": Unicode(allow_none=True),
                        "autoscale": Dict(
                            per_key_traits={
                                "min_workers": Int(allow_none=False),
                                "max_workers": Int(allow_none=False),
                                "mode": Unicode(
                                    default_value="ENHANCED", allow_none=True
                                ),
                            },
                            allow_none=True,
                        ),
                        "num_workers": Int(default_value=2, allow_none=True),
                        "apply_policy_default_values": Bool(allow_none=True),
                    }
                )
            )
        )
    ).tag(config=True)
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
