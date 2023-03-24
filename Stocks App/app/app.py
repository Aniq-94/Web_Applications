# main app file
# contains the main function and suer itneraction rules
from app.domain.Stock import Stock
from app.domain.Industry import Industry
from app.domain.exceptions.InvalidIndustry import InvalidIndustry
from app.domain.exceptions.InvalidStock import InvalidStock
from app.utils.stockreader import convert_stocks, convert_industries
import app.utils.stockutils as stockutils


def main():
    print('Welcome to the Stocks App.')
    stock_file_path = r'C:\Users\aniqa\Desktop\Courses\Semester_2\Web_Applications\assignment-1\assignment1-Aniq-94\assignment1-Aniq-94\resources\stock_returns.txt'
    industry_file_path = r'C:\Users\aniqa\Desktop\Courses\Semester_2\Web_Applications\assignment-1\assignment1-Aniq-94\assignment1-Aniq-94\resources\stock_industry.txt'
    with open(stock_file_path, 'r') as f:
        lines = f.readlines()
        stocks: list[Stock] = convert_stocks(lines[1:])
    with open(industry_file_path, 'r') as f:
        lines = f.readlines()
        industries: list[Industry] = convert_industries(lines[1:])

    while True:
        print_menu()
        user_selection = input()
        if user_selection == '0':
            break
        if user_selection == '1':
            print('List of distinct tickers:')
            print(stockutils.get_distinct_stocks(stocks))
            print('--------')
        if user_selection == '2':
            ticker = input(
                'Please enter the ticker you would like the stats for:\n')
            try:
                output = stockutils.get_stock_stats(stocks, ticker)
                print(f'Min, Max and Avg Daily Return for ticker: {ticker}')
                print(output)
                print('--------')
            except:
                print(
                    f'The stock selected is not present in the data.\nPlease select from the following list of stocks: {stockutils.get_distinct_stocks(stocks)}')
        if user_selection == '3':
            industry = input(
                'Please enter the industry you would like the stats for:\n')
            try:
                output = stockutils.get_industry_stats(stocks, industries, industry)
                print(
                    f'Min, Max and Average Daily Returns for industry: {industry}:')
                print(output)
                print('--------')
            except:
                print(
                    f'The industry selected is not present in the data.\nPlease select from the following list of industries: {stockutils.get_distinct_industry(industries)}')
        elif user_selection not in ('0','1','2','3'):
            print('Invalid Selection.')

def print_menu():
    print('Please select fromt the options below:')
    print('1. Get a list of unique Tickers.')
    print('2. Get the Min, Max and Avg Daily Return of a given ticker.')
    print('3. Get the Min, Max and Avg Daily Return for all stocks in a given industry.')
    print('0. Exit')


main()
