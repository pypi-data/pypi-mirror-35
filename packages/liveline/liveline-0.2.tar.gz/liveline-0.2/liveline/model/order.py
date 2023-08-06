from typing import Generic, TypeVar
from enum import Enum
from .equity import Equity


E = TypeVar('E', bound=Equity)


class OrderType(Enum):
    MARKET = 0
    LIMIT = 1
    STOP = 2

    def __str__(self):
        return self.name


class OrderStatus(Enum):
    PENDING = 0
    FULFILLED = 1
    CANCELED = 2
    FAILED = 3

    def __str__(self):
        return self.name


# pylint: disable=E1136
class Order(Generic[E]):
    def __init__(self,
                 equity: E,
                 quantity,
                 price,
                 order_type: OrderType=OrderType.MARKET,
                 order_status: OrderStatus=OrderStatus.PENDING):
        self._equity = equity
        self._quantity = quantity
        self._price = price
        self._order_type = order_type
        self._order_status = order_status

    def __repr__(self):
        return 'x%d $%.2f %s <%s>' % (self.quantity, self.price, self.order_type, self.equity)

    @property
    def equity(self) -> E:
        return self._equity

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def price(self) -> float:
        return self._price

    @property
    def order_type(self) -> OrderType:
        return self._order_type

    @property
    def order_status(self) -> OrderStatus:
        return self._order_status
