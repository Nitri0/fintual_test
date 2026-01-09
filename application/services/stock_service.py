from application.dto.stock.stock_dto import StockDto
from domain.repository.istock_repository import IStockTypeRepository


class StockService:
    stock_repository: IStockTypeRepository

    def __init__(self, stock_repository: IStockTypeRepository):
        self.stock_repository = stock_repository

    def get_all(self) -> list[StockDto]:
        result: list[StockDto] = []
        stocks = self.stock_repository.get_all()
        for stock in stocks:
            result.append(
                StockDto(
                    id=stock.id,
                    name=stock.name,
                    symbol=stock.symbol,
                    price=stock.price.get_value(),
                    currency=stock.price.currency.name,
                )
            )
        return result
