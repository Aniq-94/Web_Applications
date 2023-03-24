import unittest
from app.domain.Stock import Stock


class StockTest(unittest.TestCase):
    def test_eq(self):
        obj1 = Stock('MSFT', 100.00, 102.00)
        obj2 = Stock('MSFT', 100.00, 102.00)
        self.assertTrue(obj1.__eq__(obj2))

    def test_not_eq(self):
        obj1 = Stock('MSFT', 100.00, 102.00)
        obj2 = Stock('MSFT', 101.00, 102.00)
        self.assertFalse(obj1.__eq__(obj2))


if __name__ == '__main__':
    unittest.main()
