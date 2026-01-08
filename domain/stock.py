from enum import Enum

from domain.price import Price


class StockType:
    name: str


class Stock:
    stock_type: StockType
    price: Price
    quantity: int

    def __init__(self, price: Price):
        self.price = price

    def current_price(self) -> float:
        return self.price.get_value()
