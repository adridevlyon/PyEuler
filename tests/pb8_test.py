import unittest
from problems.pb8 import Pb8


class Pb8Test(unittest.TestCase):
    def test_given_large_number_when_getting_greatest_product_of_4_adjacent_digits_then_result_is_5832(self):
        pb = Pb8()
        self.assertEqual(5832, pb.greatest_product(4))

    def run_all(self):
        unittest.main()
