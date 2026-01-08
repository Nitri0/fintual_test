from dataclasses import dataclass
from typing import Tuple

from domain.allocation_stock import AllocatedStock
from domain.operation import Operation
from domain.operation_type import OperationType
from domain.stock import Stock, StockType


@dataclass
class Portfolio:
    id: str
    stocks: list[Stock]
    allocated_stocks: list[AllocatedStock]
    tolerance: float

    def __post_init__(self):
        if not len(self.stocks):
            raise ValueError("Stocks cannot be empty")

        if not len(self.allocated_stocks):
            raise ValueError("Allocated stocks cannot be empty")

        if not self.id:
            id = "id_generated"

        if not self.tolerance:
            self.tolerance = 0.1



    def rebalance(self) -> list[Operation]:
        operations: list[Operation] = []
        allocated_stocks_dict = self._convert_allocated_stocks_to_dict()

        amount_of_investment = 0
        for stock in self.stocks:
            amount_of_investment += stock.current_price() * stock.quantity

        for stock in self.stocks:
            allocated_stock_percent = allocated_stocks_dict.get(stock.type, 0)
            current_stock_percent = stock.current_price() * stock.quantity / amount_of_investment
            diference_percent = ( allocated_stock_percent - current_stock_percent)

            if diference_percent > 0:
                if diference_percent < self.tolerance:
                    continue

                # calcula el monto del capital relativo a la inversion
                amount_to_operate = amount_of_investment * abs((diference_percent - self.tolerance/2))

                # calcula el la cantidad de stocks a comprar
                quantity_to_change = int(amount_to_operate/stock.current_price())

                if quantity_to_change > 0:
                    operations.append(
                        Operation(
                            type=OperationType.COMPRA,
                            stock=stock,
                            quantity=quantity_to_change
                        )
                    )

            if diference_percent < 0:
                if abs(diference_percent) < self.tolerance:
                    continue

                amount_to_operate = amount_of_investment * abs((diference_percent - self.tolerance / 2))
                quantity_to_change = int(amount_to_operate/stock.current_price())

                if quantity_to_change > 0:
                    operations.append(
                        Operation(
                            type=OperationType.VENTA,
                            stock=stock,
                            quantity=quantity_to_change
                        )
                    )

            # como debo redistribuir los stocks?

        return operations

    def _get_current_stock_distribution(self) -> dict[StockType, float]:
        allocation_stocks: dict[StockType, float] = {}
        inversion = 0

        for stock in self.stocks:
            inversion += stock.current_price() * stock.quantity

        for stock in self.stocks:
            partition = stock.current_price() * stock.quantity / inversion
            allocation_stocks.setdefault(stock.type, partition)

        return allocation_stocks

    def _convert_allocated_stocks_to_dict(self)-> dict[StockType, float]:
        allocation_stocks: dict[StockType, float] = {}

        for allocated_stock in self.allocated_stocks:
            allocation_stocks.setdefault(allocated_stock.stock_type, allocated_stock.percent)

        return allocation_stocks