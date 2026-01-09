from domain.portfolio import Portfolio
from domain.repository.iportfolio_repository import IPortfolioRepository
from domain.stock import Stock


class MemoryPortfolioRepository(IPortfolioRepository):
    portfolios: dict[str, Portfolio]

    def __init__(self, portfolios: list[Portfolio] = None):
        self.portfolios = {}

        if portfolios is not None:
            for portfolio in portfolios:
                self.portfolios.setdefault(portfolio.id, portfolio)

    def create(self, portfolio: Portfolio) -> str:
        self.portfolios.setdefault(portfolio.id, portfolio)
        return portfolio.id

    def get_by_id(self, id: str) -> Portfolio:
        return self.portfolios.get(id)

    def get_all(self) -> list[Portfolio]:
        return list(self.portfolios.values())
