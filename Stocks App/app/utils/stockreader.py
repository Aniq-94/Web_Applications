from app.domain.Stock import Stock
from app.domain.Industry import Industry
from app.domain.exceptions.InvalidStock import InvalidStock
from app.domain.exceptions.InvalidIndustry import InvalidIndustry


def convert_stocks(stocks: list[str]) -> list[Stock]:
    results: list[Stock] = []
    for stock in stocks:
        validate_stocks(stock)
        ticker, open_price, close_price = stock.split(",")
        stock_return = (float(close_price)-float(open_price))/float(open_price)
        results.append(Stock(ticker, float(open_price), float(close_price)))
        # it validates the input, if the input is valid it appends it to the result list,
        # if not it will throw an exception through the validate stock function
    return results


def validate_stocks(stock: str) -> None:
    '''Given a string representation of a stock object, this function returns None if the string is valid'''
    elements: list[str] = stock.split(",")
    if len(elements) != 3:
        raise InvalidStock(
            f'Expected three elements but found {len(elements)}')
    ticker, open_price, close_price = elements
    try:
        float(open_price)
        float(close_price)
    except:
        raise InvalidStock(
            f'Expected data type: str, float, float. Found: {stock}')


def convert_industries(industries: list[str]) -> list[Industry]:
    results: list[Industry] = []
    for industry in industries:
        validate_industries(industry)
        ticker, industry = industry.split(",")
        results.append(Industry(ticker, industry.replace("\n", "")))
    return results


def validate_industries(industry: str) -> None:
    elements: list[str] = industry.split(",")
    if len(elements) != 2:
        raise InvalidIndustry(
            f'Expected two elements but found {len(elements)}')
