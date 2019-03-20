import unittest
from Problems.pb1 import Pb1


class Pb1Test(unittest.TestCase):
    def test_given_multiples_of_3_and_5_when_ceiling_is_10_sum_is_23(self):
        pb = Pb1()
        self.assertEqual(23, pb.get_multiples_sum([3, 5], 10))


if __name__ == '__main__':
    unittest.main()
