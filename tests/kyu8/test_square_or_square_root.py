import unittest
from codewars import IMPLEMENTATIONS


class TestSquareOrSquareRootSolutions(unittest.TestCase):
    test_cases = [
        ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
        ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
        ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]),
    ]

    def test_all_square_or_square_root(self):
        for name, kyu in IMPLEMENTATIONS.items():
            for arr, expected in self.test_cases:
                result = kyu["kyu8"].square_or_square_root(arr)
                msg = "[{}] input: {}, got: {}, expected: {}".format(name, arr, result, expected)
                self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
