import unittest
from problems.pb15 import Pb15


class Pb15Test(unittest.TestCase):
    def test_given_a_2x2_grid_when_counting_path_from_top_left_to_bottom_right_then_count_is_6(self):
        pb = Pb15()
        self.assertEqual(6, pb.count_paths_in_grid(2))

    def run_all(self):
        unittest.main()
