from application.dto.stock_dto import StockDto
from domain.currency import Currency
from domain.price import Price
from domain.repository.istock_repository import IStockTypeRepository
from domain.stock import StockType


class StockMapper:
    @staticmethod
    def console_dto_to_domain(dto: StockDto) -> StockType:
        return StockType(
            id=dto.id,
            name=dto.name,
            symbol=dto.symbol,
            price=Price(
                value=dto.price,
                currency=Currency(dto.currency)
            )
        )


class MemoryStockTypeRepository(IStockTypeRepository):
    stocks_dic: dict[str, StockType]

    def __init__(self, stocks: list[StockDto] = None):
        self.stocks_dic = {}
        if stocks is not None:
            for stock in stocks:
                self.stocks_dic.setdefault(
                    stock.id,
                    StockMapper.console_dto_to_domain(stock)
                )

    def get_all(self) -> list[StockType]:
        return list(self.stocks_dic.values())
