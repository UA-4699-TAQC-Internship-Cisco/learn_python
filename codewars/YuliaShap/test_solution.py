import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from kyu8 import litres as litres_1
from ..Dbautista.codewars_tasks_8kyu import litres as litres_2
from ..mpeshko.ky8 import litres as litres_3
from ..TYakushevych.ky8 import litres as litres_4
# from student5.solution import litres as litres_5
# from student6.solution import litres as litres_6
# from student7.solution import litres as litres_7
# from student8.solution import litres as litres_8


class TestLitresSolutions(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            ('Dbautista', litres_1),
            ('mpeshko', litres_2),
            ('TYakushevych', litres_3),
            ('YuliaShap', litres_4),
            # ('student5', litres_5),
            # ('student6', litres_6),
            # ('student7', litres_7),
            # ('student8', litres_8),
        ]

        self.test_cases = [
            (0, 0),
            (0.5, 0),
            (1, 0),
            (2, 1),
            (3, 1),
            (6.7, 3),
            (11.8, 5),
            (1787, 893),
            (float('1e6'), 500000),
        ]

    def test_all_solutions(self):
        for name, func in self.solutions:
            print("\nTesting solution: {}".format(name))
            for time, expected in self.test_cases:
                result = func(time)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, time, result, expected))
                self.assertEqual(result, expected, msg)
            print("Solution '{}' passed all tests!".format(name))


if __name__ == '__main__':
    unittest.main()

