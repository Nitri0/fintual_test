import abc
from domain.stock import StockType


class IStockTypeRepository:

    @abc.abstractmethod
    def get_all(self) -> list[StockType]:
        ...
