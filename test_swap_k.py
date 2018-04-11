import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_zero(self):
        """ Test swap_k when k is 0"""

        actual = a1.swap_k([1, 2, 3, 4, 5], 0)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected,actual)

    def test_swap_k_list_odd_length(self):
        """ Test swap_k when k is equal to len(L) // 2 and this length is odd"""

        actual = a1.swap_k([1, 2, 3, 4, 5, 6, 7], 3)
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(expected,actual)

    def test_swap_k_list_even_length(self):
        """ Test swap_k when k is equal to len(L) // 2 and this length is even"""

        actual = a1.swap_k([1, 2, 3, 4, 5, 6, 7, 8], 4)
        expected = [ 5, 6, 7, 8, 1, 2, 3, 4]
        self.assertEqual(expected,actual)

    def test_swap_k_(self):
        """ Test swap_k when k and list L are not extremes of preconditions."""

        actual = a1.swap_k([1, 2, 3, 4, 5, 6, 7, 8], 1)
        expected = [ 8, 2, 3, 4, 5, 6, 7, 1]
        self.assertEqual(expected,actual)

    def test_swap_k_empty_list(self):
        """ Test swap_k when list L is empty"""

        actual = a1.swap_k([], 0)
        expected = []
        self.assertEqual(expected,actual)

    def test_swap_k_list_not_sorted(self):
        """ Test swap_k when list L is not sorted and k is equal to 1"""

        actual = a1.swap_k([1, 3, 5, 4, 10, 6, 8, 9], 3)
        expected = [6, 8, 9,4, 10, 1, 3, 5]
        self.assertEqual(expected,actual)
if __name__ == '__main__':
    unittest.main(exit=False)