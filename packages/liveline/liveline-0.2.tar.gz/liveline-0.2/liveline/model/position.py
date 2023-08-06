from .equity import Equity


class Position:
    def __init__(self):
        pass

    @property
    def equity(self) -> Equity:
        pass

    @property
    def quantity(self) -> float:
        pass
