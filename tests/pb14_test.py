import unittest
from problems.pb14 import Pb14


class Pb14Test(unittest.TestCase):
    def test_given_collatz_sequence_when_start_with_13_then_squence_length_is_10(self):
        pb = Pb14()
        self.assertEqual(10, pb.collatz_sequence_length(13))

    def run_all(self):
        unittest.main()
