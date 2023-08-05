from ._county import WriteCounty
from ._district import WriteDistrict
from ._state import WriteState


class Writer(WriteCounty, WriteDistrict, WriteState):
    pass
