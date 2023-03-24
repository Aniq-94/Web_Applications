import unittest
from app.domain.Stock import Stock
from app.domain.Industry import Industry
from app.domain.exceptions.InvalidIndustry import InvalidIndustry
from app.domain.exceptions.InvalidStock import InvalidStock
from app.utils.stockreader import validate_stocks, convert_stocks, validate_industries, convert_industries


class StockReaderTest(unittest.TestCase):
    def test_validate_stocks(self):
        input = 'AAPL,100.00,102.00'  # valid input
        self.assertIsNone(validate_stocks(input))

    def test_validate_stocks_invalid_size(self):
        input = 'AAPL,100.00,102.00,ExtraField'
        self.assertRaises(InvalidStock, validate_stocks, input)

    def test_validate_stocks_data_type(self):
        input = 'AAPL,s100.00,102.00'
        self.assertRaises(InvalidStock, validate_stocks, input)
        input = 'AAPL,100.00,102.00s'
        self.assertRaises(InvalidStock, validate_stocks, input)

    def test_convert_stocks(self):
        input = [
            'AAPL,100.00,102.00',
            'MSFT,100.00,102.00',
            'TSLA,1000.00,1200.00'
        ]
        stock = Stock('MSFT', 100.00, 102.00)
        output = convert_stocks(input)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) != 0)
        self.assertEqual(len(output), 3)
        self.assertTrue(isinstance(output[0], Stock))
        self.assertEqual(stock, output[1])

    def test_validate_industries(self):
        input = 'AAPL, TECH'
        self.assertIsNone(validate_industries(input))

    def test_validate_industries_invalid_size(self):
        input = 'AAPL,TECH,ExtraDataField'
        self.assertRaises(InvalidIndustry, validate_industries, input)

    def test_convert_industries(self):
        input = ['AAPL,TECH',
                 'MSFT,TECH',
                 'TSLA,AUTOMOBILES']
        industry = Industry('MSFT', 'TECH')
        output = convert_industries(input)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) != 0)
        self.assertEqual(len(output), 3)
        self.assertTrue(isinstance(output[0], Industry))
        self.assertEqual(industry, output[1])


if __name__ == '__main__':
    unittest.main()
