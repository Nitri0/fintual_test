
from application.services.portfolio_service import PortfolioService
from domain.allocation_stock import AllocatedStock
from domain.currency import Currency
from domain.operation_type import OperationType
from domain.portfolio import Portfolio
from domain.price import Price
from domain.stock import Stock, StockType
from infrastructure.persistence.memory.memory_portfolio_repository import MemoryPortfolioRepository

def main():

    stocks_type: dict[str, StockType] = {
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

    stocks: list[Stock] = [
        Stock(
            id="id",
            type=stocks_type.get("APPLE"),
            quantity=10000,
        ),
        Stock(
            id="id",
            type=stocks_type.get("META"),
            quantity=500,
        ),
    ]

    allocated_stocks: list[AllocatedStock] = [
        AllocatedStock(
            stock_type=stocks_type.get("APPLE"),
            percent=0.25
        ),
        AllocatedStock(
            stock_type=stocks_type.get("META"),
            percent=0.75
        )
    ]

    portfolio = Portfolio(
        id="1",
        name="Default Portfolio",
        stocks=stocks,
        allocated_stocks=allocated_stocks,
        tolerance=0.01
    )

    portfolio_repository = MemoryPortfolioRepository(
        portfolios=[portfolio]
    )
    portfolio_service = PortfolioService(portfolio_repository)
    operations = portfolio_service.rebalance_portfolio(
        portfolio.id
    )

    total_inversion = sum(stock.quantity * stock.current_price() for stock in stocks)

    print('\nCurrent distribution:')
    for distribution in stocks:
        percent =distribution.quantity * distribution.current_price() / total_inversion
        print(f'    * {distribution.type.name} with {distribution.quantity} represent {percent:.2f} %')

    print('\nExpected distribution:')
    for distribution in allocated_stocks:
        print(f'    * {distribution.stock_type.name} should representate {distribution.percent}%')

    print("\nFor redistribute the stocks, should do the next actions:")
    for operation in operations:
        print(f'    * {operation.type.name} {operation.stock.type.name} {operation.quantity} stocks')


    print("\nWhen apply this operations the distribution should be:")
    for operation in operations:
        if operation.type == OperationType.COMPRA:
            total_quantity = operation.stock.quantity + operation.quantity
        else:
            total_quantity = operation.stock.quantity - operation.quantity

        percent = total_quantity * operation.stock.current_price() / total_inversion
        print(f'    * {operation.stock.type.name} with {total_quantity} stock that represent {percent:.2f}')

    print("\nYou could change allocated_stocks config for test other results.")
    print("You could change the stock quantity in the portfolio for add a new current distribution.")
    print("You could change the tolerance in portfolio for change the range expected.")


if __name__ == '__main__':
    main()