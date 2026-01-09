from application.dto.portfolio.portfolio_dto import PortfolioDto
from domain.operation import Operation
from domain.repository.iportfolio_repository import IPortfolioRepository


class PortfolioService:
    portfolio_repository: IPortfolioRepository

    def __init__(self, portfolio_repository: IPortfolioRepository):
        self.portfolio_repository = portfolio_repository

    def rebalance_portfolio(self, id: str) -> list[Operation]:
        portfolio = self.portfolio_repository.get_by_id(id)
        operations = portfolio.rebalance()

        return operations

    def get_all_portfolios(self) -> list[PortfolioDto]:
        results_dto : list[PortfolioDto] = []
        portfolios = self.portfolio_repository.get_all()

        for portfolio in portfolios:
            results_dto.append(
                PortfolioDto(
                    id=portfolio.id,
                    name=portfolio.name,
                )
            )

        return results_dto
