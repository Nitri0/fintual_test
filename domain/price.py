from dataclasses import dataclass

from domain.currency import Currency

@dataclass
class Price:
    value: float
    currency: Currency

    def __str__(self):
        return f"{self.value} {self.currency.name}"

    def get_value(self):
        return self.value

