from domain.currency import Currency


class Price:
    value: float
    currency: Currency

    def get_value(self):
        return self.value
