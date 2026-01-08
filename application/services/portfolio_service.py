import json

from domain.operation import Operation
from domain.portfolio import Portfolio
from domain.repository.iportfolio_repository import IPortfolioRepository


class PortfolioService:
    portfolio_repository: IPortfolioRepository

    def __init__(self, portfolio_repository: IPortfolioRepository):
        self.portfolio_repository = portfolio_repository

    def rebalance_portfolio(self, id: str) -> list[Operation]:
        portfolio = self.portfolio_repository.get_by_id(id)
        operations = portfolio.rebalance()

        return operations
