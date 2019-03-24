import unittest
from problems.pb2 import Pb2


class Pb2Test(unittest.TestCase):
    def test_given_fibonacci_sequence_when_ceiling_is_90_sum_of_even_terms_is_44(self):
        pb = Pb2()
        self.assertEqual(44, pb.get_sum_of_even_terms_less_than(90))


if __name__ == '__main__':
    unittest.main()
