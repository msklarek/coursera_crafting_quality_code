import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty_list(self):
        """ Test stock_price_summary with empty list of price_changes"""

        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(expected,actual)

    def test_stock_price_summary_one_positive(self):
        """ Test stock_price_summary with list containing one positive item """

        actual = a1.stock_price_summary([0.02])
        expected = (0.02,0)
        self.assertEqual(expected,actual)

    def test_stock_price_summary_one_negative(self):
        """ Test stock_price_summary with list containing one negative item"""

        actual = a1.stock_price_summary([-0.02])
        expected = (0, -0.02)
        self.assertEqual(expected,actual)


    def test_stock_price_summary_mix(self):
        """ Test stock_price_summary with list of negative, positive and zero item."""

        actual = a1.stock_price_summary([-0.01, -0.03, -0.10, 0.01, 0.03, 0.10, 0])
        expected = (0.14, -0.14)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main(exit=False)