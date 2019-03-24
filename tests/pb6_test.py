import unittest
from problems.pb6 import Pb6


class Pb6Test(unittest.TestCase):
    def test_given_difference_between_square_of_sum_and_sum_of_squares_when_values_below_10_then_result_is_2640(self):
        pb = Pb6()
        self.assertEqual(2640, pb.difference_squares_and_sum(10))

    def run_all(self):
        unittest.main()
