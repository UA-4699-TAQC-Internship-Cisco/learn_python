import unittest

from codewars import IMPLEMENTATIONS


class TestLitresSolutions(unittest.TestCase):
    test_cases = [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (1.4, 0),
        (12.3, 6),
        (0.82, 0),
        (11.8, 5),
        (1787, 893),
    ]

    def test_all_litres(self):

        for name, kyu in IMPLEMENTATIONS.items():
            for time, expected in self.test_cases:
                result = kyu["kyu8"].litres(time)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, time, result, expected))
                self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
