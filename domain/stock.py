from dataclasses import dataclass
from enum import Enum

from domain.price import Price


@dataclass
class StockType:
    id: str
    name: str
    symbol: str
    price: Price

    def __hash__(self):
        return hash(self.name)


@dataclass
class Stock:
    id: str
    type: StockType
    quantity: int

    def current_price(self) -> float:
        return self.type.price.get_value()
