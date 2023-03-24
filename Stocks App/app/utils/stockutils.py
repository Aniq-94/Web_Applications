from app.domain.Stock import Stock
from app.domain.Industry import Industry


def get_distinct_stocks(stocks: list[Stock]) -> set[str]:
    unique_stocks: set[str] = set()
    for stock in stocks:
        unique_stocks.add(stock.ticker)
    return unique_stocks


def get_stock_stats(stocks: list[Stock], stock_ticker: str) -> tuple[float, float, float]:
    stocks = filter_on_ticker(stocks, stock_ticker)
    stock_returns: list[float] = []
    for stock in stocks:
        stock_returns.append(stock.stock_return)
    return (min(stock_returns), max(stock_returns), sum(stock_returns)/len(stock_returns))


def filter_on_ticker(stocks: list[Stock], stock_ticker: str) -> list[Stock]:
    result: list[Stock] = []
    for stock in stocks:
        if stock.ticker == stock_ticker:
            result.append(stock)
    return result


def get_industry_stats(stocks: list[Stock], industries: list[Industry], ind_name: str) -> tuple[float, float, float]:
    ticker_to_industry: dict[str:str] = {}
    for stock in stocks:
        ticker_to_industry[stock.ticker] = get_industry(
            industries, stock.ticker)
    stocks = filter_on_industry(stocks, ind_name, ticker_to_industry)
    stats: list[float] = []
    for stock in stocks:
        stats.append(stock.stock_return)
    return (min(stats), max(stats), sum(stats)/len(stats))


def filter_on_industry(stocks: list[Stock], industry: str, ticker_to_industry: dict[str:str]) -> list[Stock]:
    result: list[Stock] = []
    for stock in stocks:
        stock_industry = ticker_to_industry.get(stock.ticker)
        if stock_industry == industry:

            result.append(stock)
    return result


def get_industry(industries: list[Industry], ticker: str) -> str:
    for i in industries:
        if i.ticker == ticker:
            return i.industry


def get_distinct_industry(industries: list[Industry]) -> set[str]:
    unique_industries = set()
    for i in industries:
        unique_industries.add(i.industry)
    return unique_industries
