class Industry():
    def __init__(self, ticker: str, industry: str):
        self.ticker = ticker
        self.industry = industry

    def __eq__(self, other) -> bool:
        return isinstance(other, Industry) and other.ticker == self.ticker and other.industry == self.industry
