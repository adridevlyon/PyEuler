import unittest
from problems.pb12 import Pb12


class Pb12Test(unittest.TestCase):
    def test_given_triangular_numbers_when_over_5_divisors_then_value_is_28(self):
        pb = Pb12()
        self.assertEqual(28, pb.first_triangle_number_with_n_divisors(5))

    def run_all(self):
        unittest.main()
