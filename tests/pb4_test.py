import unittest
from problems.pb4 import Pb4


class Pb4Test(unittest.TestCase):
    def test_given_palindrom_produts_of_two_factors_when_factors_less_than_100_then_largest_is_9009(self):
        pb = Pb4()
        self.assertEqual(9009, pb.largest_palindrom_with_factors_at_most(99))

    def run_all(self):
        unittest.main()
