import unittest

from codewars import IMPLEMENTATIONS


class TestDivisibleBySolutions(unittest.TestCase):
    test_cases = [
        (([1, 2, 3, 4, 5, 6], 2), [2, 4, 6]),
        (([1, 2, 3, 4, 5, 6], 3), [3, 6]),
        (([0, 1, 2, 3, 4, 5, 6], 4), [0, 4]),
        (([0], 4), [0]),
        (([1, 3, 5], 2), [])
    ]

    def test_all_divisible_by(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution for divisible: {}".format(name)
            for (numbers, divisor), expected in self.test_cases:
                result = kyu["kyu8"].divisible_by(numbers, divisor)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, (numbers, divisor), result, expected))
                self.assertEqual(result, expected, msg)
            print "Solution '{}' passed all tests!".format(name)


if __name__ == '__main__':
    unittest.main()
