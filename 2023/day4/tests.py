from functions import line_to_winning_numbers, line_to_obtained_numbers, compute_points
import unittest

class TestFunctions(unittest.TestCase):

    def test_line_to_winning_numbers(self):
        self.assertEqual(line_to_winning_numbers('Card 3:  1 21 59 44 | 69 72 16 21 14 1'), [1, 21, 59, 44])

    def test_line_to_obtained_numbers(self):
        self.assertEqual(line_to_obtained_numbers('Card 3:  1 21 59 44 | 69 72 16 21 14 1'), [69, 72, 16, 21, 14, 1])

    def test_compute_points(self):
        self.assertEqual(compute_points([1,2,3,4], [3,4,5,6]), 2)

if __name__ == '__main__':
    unittest.main()