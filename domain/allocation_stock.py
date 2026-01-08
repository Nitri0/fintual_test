from domain.stock import  StockType


class AllocatedStock:
    stock_type: StockType
    percent: float

    def __init__(self, stock: StockType, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 1 and 100")

        self.stock_type = stock
        self.percent = percent
