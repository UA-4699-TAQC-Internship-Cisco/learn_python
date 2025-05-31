import unittest
from codewars import IMPLEMENTATIONS


class TestFindNbSolutions(unittest.TestCase):
    test_cases = [
        (4, -1),
        (16, -1),
        (4183059834009, 2022),
        (24723578342962, -1),
        (135440716410000, 4824),
        (40539911473216, 3568),
        (26825883955641, 3218)
    ]

    def test_all_find_nb(self):
        for name, kyu in IMPLEMENTATIONS.items():
            for n, expected in self.test_cases:
                result = kyu["kyu6"].find_nb(n)
                msg = "[{}] input: {}, got: {}, expected: {}".format(name, n, result, expected)
                self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
