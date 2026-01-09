import unittest
from unittest.mock import Mock

from application.services.portfolio_service import PortfolioService
from domain.allocation_stock import AllocatedStock
from domain.currency import Currency
from domain.operation_type import OperationType
from domain.portfolio import Portfolio
from domain.price import Price
from domain.repository.iportfolio_repository import IPortfolioRepository
from domain.stock import Stock, StockType


class PortfolioServiceTest(unittest.TestCase):
    def setUp(self):
        portfolio_mock_repo = Mock(spec=IPortfolioRepository)
        stock_dict = {
            "APPLE": StockType(
                id="1",
                name="APPLE",
                symbol="APPLE",
                price=Price(
                    value=2.0,
                    currency=Currency("USD")
                ),
            ),
            "META": StockType(
                id="2",
                name="META",
                symbol="META",
                price=Price(
                    value=1.0,
                    currency=Currency("USD")
                ),
            )
        }

        portfolio_mock_repo.get_by_id.return_value = Portfolio(
            id="id",
            name="default portfolio",
            stocks=[
                Stock(
                    id="id",
                    type=stock_dict.get("APPLE"),
                    quantity=10000,
                ),
                Stock(
                    id="id",
                    type=stock_dict.get("META"),
                    quantity=500,
                ),
            ],
            allocated_stocks=[
                AllocatedStock(
                    stock_type=stock_dict.get("APPLE"),
                    percent=0.25
                ),
                AllocatedStock(
                    stock_type=stock_dict.get("META"),
                    percent=0.75
                )
            ],
            tolerance=0.001
        )

        self.portfolio_service = PortfolioService(portfolio_mock_repo)

    def test_when_a_portfolio_rebalance_should_returns_valid_operations(self):
        operations = self.portfolio_service.rebalance_portfolio("id_ramdom")

        assert operations[0].stock.type.name == "APPLE"
        assert operations[0].quantity == 7442  # -> Valor restando tolerancia/2
        assert operations[0].type == OperationType.VENTA

        assert operations[1].stock.type.name == "META"
        assert operations[1].quantity == 14864  # -> Valor restando tolerancia/2
        assert operations[1].type == OperationType.COMPRA

