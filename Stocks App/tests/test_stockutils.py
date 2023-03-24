import unittest
from app.domain.Stock import Stock
from app.domain.Industry import Industry
from app.utils.stockutils import get_distinct_stocks, filter_on_ticker, get_stock_stats, get_industry, filter_on_industry, get_industry_stats


class StockUtilsTest(unittest.TestCase):
    def test_get_distinct_stocks(self):
        input = [
            Stock('MSFT', 100.00, 102.00),
            Stock('TSLA', 100.00, 102.00),
            Stock('F', 100.00, 102.00),
            Stock('MSFT', 100.00, 102.00),
            Stock('AMZN', 100.00, 102.00),
            Stock('TSLA', 100.00, 102.00)
        ]
        output = get_distinct_stocks(input)
        self.assertIsNotNone(output)
        self.assertEqual(4, len(output))
        self.assertEqual({'MSFT', 'TSLA', 'F', 'AMZN'}, output)

    def test_filter_on_ticker(self):
        input = [Stock('MSFT', 100.00, 102.00),
                 Stock('TSLA', 100.00, 102.00),
                 Stock('AMZN', 100.00, 102.00),
                 Stock('F', 100.00, 102.00),
                 Stock('MSFT', 100.00, 102.00),
                 Stock('MSFT', 100.00, 102.00)]
        ticker = 'MSFT'
        output = filter_on_ticker(input, ticker)
        self.assertIsNotNone(output)
        self.assertEqual(3, len(output))
        for i in output:
            self.assertEqual(i.ticker, 'MSFT')

    def test_get_stock_stats(self):
        input = [Stock('MSFT', 100.00, 105.00),
                 Stock('TSLA', 100.00, 102.00),
                 Stock('AMZN', 100.00, 102.00),
                 Stock('F', 100.00, 102.00),
                 Stock('MSFT', 100.00, 110.00),
                 Stock('MSFT', 100.00, 107.50)]
        ticker = 'MSFT'
        output = get_stock_stats(input, ticker)
        self.assertIsNotNone(output)
        self.assertTrue(isinstance(output, tuple))
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], 5.00)
        self.assertEqual(output[1], 10.00)
        self.assertEqual(output[2], 7.50)

    def test_get_industry(self):
        industries = [Industry('MSFT', 'TECH'),
                      Industry('BA', 'AVIATION')]
        self.assertEqual(get_industry(industries, 'MSFT'), 'TECH')
        self.assertEqual(get_industry(industries, 'BA'), 'AVIATION')
        self.assertIsNone(get_industry(industries, 'INVALID_INPUT'))

    def test_filter_on_industry(self):
        input = [Stock('MSFT', 100.00, 102.00),
                 Stock('AMZN', 100.00, 102.00),
                 Stock('F', 105.00, 110.00),
                 Stock('F', 100.00, 110.00),
                 Stock('MSFT', 100.00, 102.00),
                 Stock('AMZN', 105.00, 107.00),]
        ticker_to_industry = {'MSFT': 'TECH',
                              'AMZN': 'TECH',
                              'F': 'AUTO'
                              }
        output = filter_on_industry(input, 'TECH', ticker_to_industry)
        self.assertIsNotNone(output)
        self.assertEqual(4, len(output))
        output = filter_on_industry(input, 'AUTO', ticker_to_industry)
        self.assertIsNotNone(output)
        self.assertEqual(2, len(output))

    def test_get_industry_stats(self):
        input = [Stock('MSFT', 100.00, 101.00),
                 Stock('AMZN', 100.00, 103.00),
                 Stock('F', 105.00, 110.00),
                 Stock('F', 100.00, 110.00),
                 Stock('MSFT', 100.00, 103.00),
                 Stock('AMZN', 100.00, 105.00),]
        industries = [Industry('MSFT', 'TECH'),
                      Industry('AMZN', 'TECH'),
                      Industry('F', 'AUTO')]
        output: tuple[float, float, float] = get_industry_stats(
            input, industries, 'TECH')
        self.assertIsNotNone(output)
        self.assertEqual(3, len(output))
        self.assertTrue((isinstance(output, tuple)))
        self.assertEqual(1.00, output[0])
        self.assertEqual(5.00, output[1])
        self.assertEqual(3.00, output[2])


if __name__ == '__main__':
    unittest.main()
