from ._nation import AggregateNation
from ._state import AggregateState
from ._variable import AggregateVariable


class Aggregator(AggregateVariable, AggregateNation, AggregateState):
    pass
