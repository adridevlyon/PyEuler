import unittest
from problems.pb9 import Pb9


class Pb9Test(unittest.TestCase):
    def test_given_pythagorean_triplet_when_sum_is_12_then_product_is_60(self):
        pb = Pb9()
        self.assertEqual(60, pb.product_of_pythagorean_triplet(12))

    def run_all(self):
        unittest.main()
