import unittest
from problems.pb3 import Pb3


class Pb3Test(unittest.TestCase):
    def test_given_13195_when_getting_prime_factors_then_largest_is_29(self):
        pb = Pb3()
        self.assertEqual(29, pb.largest_prime_factor(13195))

    def run_all(self):
        unittest.main()
