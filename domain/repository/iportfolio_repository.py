import abc

from domain.portfolio import Portfolio


class IPortfolioRepository:
    @abc.abstractmethod
    def create(self, portfolio: Portfolio) -> int:
        ...

    @abc.abstractmethod
    def get_by_id(self, id: str) -> Portfolio:
        ...
