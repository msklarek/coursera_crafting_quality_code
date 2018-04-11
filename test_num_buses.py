import a1
import unittest



class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_0_people(self):
        """Test num_buses with 0 people ."""

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected,actual)

    def test_num_buses_less_50(self):
        """Test num_buses with less than 50 people ."""

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected,actual)

    def test_num_buses_more_50(self):
        """Test num_buses with more than 50 people ."""

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected,actual)

    def test_num_buses_exactly_50(self):
        """Test num_buses with more than 50 people ."""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected,actual)
if __name__ == '__main__':
    unittest.main(exit=False)