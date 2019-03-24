import unittest
from problems.pb7 import Pb7


class Pb7Test(unittest.TestCase):
    def test_given_prime_numbers_when_getting_6th_then_result_is_13(self):
        pb = Pb7()
        self.assertEqual(13, pb.n_th_prime(6))

    def run_all(self):
        unittest.main()
