import unittest
from problems.pb10 import Pb10


class Pb10Test(unittest.TestCase):
    def test_given_primes_when_all_below_10_then_sum_is_17(self):
        pb = Pb10()
        self.assertEqual(17, pb.sum_of_primes_below(10))

    def run_all(self):
        unittest.main()
