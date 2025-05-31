import unittest
from codewars.TYakushevych import ky8 as test_count

class TestCountOfPositivesSumOfNegatives(unittest.TestCase):

    test_data = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]),
        ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], [8, -50]),
        ([1], [1, 0]),
        ([-1], [0, -1]),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0]),
        ([], [])
    ]

    def test_count_positives_valid(self):
        for actual, expected in self.test_data:
            result = test_count.count_positives_sum_negatives(actual)
            self.assertEqual(result, expected)

    def test_count_positives_return_list(self):
        self.assertIsInstance(test_count.count_positives_sum_negatives([]), list)
