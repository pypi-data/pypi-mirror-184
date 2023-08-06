from traitlets import Dict, HasTraits

from pushcart.configuration.validation.common import ExistingDeltaPath, ViewName


class DeltaSourceConfiguration(HasTraits):
    """
    Stores pipeline source configuration for a path containing a Delta table.
    """

    from_dict = Dict(
        default_value={},
        help="Dictionary containing the configuration for the pipeline",
        allow_none=True,
        per_key_traits={
            "from": ExistingDeltaPath(),
            "into": ViewName(),
        },
    )
