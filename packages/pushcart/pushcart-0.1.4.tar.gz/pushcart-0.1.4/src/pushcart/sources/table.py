from traitlets import Dict, HasTraits

from pushcart.configuration.validation.common import TableName, ViewName


class TableSource(HasTraits):
    config = Dict(per_key_traits={"from": TableName, "into": ViewName})

    def get_increment(self):
        pass
