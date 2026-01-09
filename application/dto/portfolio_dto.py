from dataclasses import dataclass


@dataclass(frozen=True)
class PortfolioDto:
    id: str
    name: str
