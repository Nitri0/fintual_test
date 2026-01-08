from domain.allocation_stock import AllocatedStock
from domain.operation import Operation
from domain.stock import Stock, StockType


class Portfolio:
    stocks: list[Stock]
    allocated_stocks: list[AllocatedStock]

    def rebalance(self) -> list[Operation]:
        operations: list[Operation] = []

        current_distribution_stocks = self._get_current_stock_distribution()

        for allocated_stock in self.allocated_stocks:
            percent = current_distribution_stocks.get(allocated_stock.stock_type, 0)
            # como debo redistribuir los stocks?

        return operations

    def _get_current_stock_distribution(self) -> dict[StockType, float]:
        allocation_stocks: dict[StockType, float] = {}
        inversion = 0

        for stock in self.stocks:
            inversion += stock.current_price() * stock.quantity

        for stock in self.stocks:
            partition = stock.current_price() * stock.quantity / inversion
            allocation_stocks.setdefault(stock.stock_type, partition)

        return allocation_stocks
