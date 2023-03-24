class Stock():
    def __init__(self, ticker: str, open_price: float, close_price: float):
        self.ticker = ticker
        self.open_price = open_price
        self.close_price = close_price
        self.stock_return = (((close_price-open_price)/(open_price))*100)

    def __eq__(self, other) -> bool:
        return isinstance(other, Stock) and other.ticker == self.ticker and other.open_price == self.open_price and other.close_price == self.close_price and other.stock_return == self.stock_return
