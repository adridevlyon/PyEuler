import unittest
from problems.pb5 import Pb5


class Pb5Test(unittest.TestCase):
    def test_given_all_values_below_10_when_computing_minimum_common_multiple_then_result_is_2520(self):
        pb = Pb5()
        self.assertEqual(2520, pb.smallest_common_multiple_for_all_numbers_below(10))


if __name__ == '__main__':
    unittest.main()
