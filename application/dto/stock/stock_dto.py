from dataclasses import dataclass


@dataclass(frozen=True)
class StockDto:
    id: str
    name: str
    symbol: str
    price: float
    currency: str
