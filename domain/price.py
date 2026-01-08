from dataclasses import dataclass

from domain.currency import Currency

@dataclass
class Price:
    value: float
    currency: Currency

    def get_value(self):
        return self.value
