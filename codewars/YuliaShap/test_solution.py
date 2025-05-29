import unittest

from codewars.YuliaShap.kyu6 import stock_list as stock_list_1
from codewars.YuliaShap.kyu8 import divisible_by as divisible_by_1
from codewars.YuliaShap.kyu8 import litres as litres_1
from ..Dbautista.codewars_tasks_6kyu import stock_list as stock_list_2
from ..Dbautista.codewars_tasks_8kyu import divisible_by as divisible_by_2
from ..Dbautista.codewars_tasks_8kyu import litres as litres_2
from ..TYakushevych.ky6 import stock_list as stock_list_4
from ..TYakushevych.ky8 import divisible_by as divisible_by_4
from ..TYakushevych.ky8 import litres as litres_4
from ..mpeshko.ky6 import stock_list as stock_list_3
from ..mpeshko.ky8 import divisible_by as divisible_by_3
from ..mpeshko.ky8 import litres as litres_3


# from student5.solution import litres as litres_5
# from student6.solution import litres as litres_6
# from student7.solution import litres as litres_7
# from student8.solution import litres as litres_8


class TestLitresSolutions(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            ('YuliaShap', litres_1),
            ('Dbautista', litres_2),
            ('mpeshko', litres_3),
            ('TYakushevych', litres_4),
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

    def test_all_solutions_1(self):
        for name, func in self.solutions:
            print "\nTesting solution for litres: {}".format(name)
            for time, expected in self.test_cases:
                result = func(time)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, time, result, expected))
                self.assertEqual(result, expected, msg)
            print "Solution '{}' passed all tests!".format(name)


class TestDivisibleBySolutions(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            ('YuliaShap', divisible_by_1),
            ('Dbautista', divisible_by_2),
            ('mpeshko', divisible_by_3),
            ('TYakushevych', divisible_by_4),
            # ('student5', divisible_by_5),
            # ('student6', divisible_by_6),
            # ('student7', divisible_by_7),
            # ('student8', divisible_by_8),
        ]

        self.test_cases = [
            (([1, 2, 3, 4, 5, 6], 2), [2, 4, 6]),
            (([1, 2, 3, 4, 5, 6], 3), [3, 6]),
            (([0, 1, 2, 3, 4, 5, 6], 4), [0, 4]),
            (([0], 4), [0]),
            (([1, 3, 5], 2), [])
        ]

    def test_all_solutions_2(self):
        for name, func in self.solutions:
            print "\nTesting solution for divisible: {}".format(name)
            for (numbers, divisor), expected in self.test_cases:
                result = func(numbers, divisor)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, (numbers, divisor), result, expected))
                self.assertEqual(result, expected, msg)
            print "Solution '{}' passed all tests!".format(name)


class TestStockListSolutions(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            ('YuliaShap', stock_list_1),
            ('Dbautista', stock_list_2),
            ('mpeshko', stock_list_3),
            ('TYakushevych', stock_list_4),
            # ('student5', stock_list_5),
            # ('student6', stock_list_6),
            # ('student7', stock_list_7),
            # ('student8', stock_list_8),
        ]

        self.test_cases = [
            ((["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], ["A", "B", "C", "W"]),
             "(A : 20) - (B : 114) - (C : 50) - (W : 0)"),
            ((["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]),
             "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"),
            ((["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]),
             "(A : 200) - (B : 1140)")
        ]

    def test_all_solutions_3(self):
        for name, func in self.solutions:
            print "\nTesting solution for stock_list: {}".format(name)
            for (stocklist, categories), expected in self.test_cases:
                result = func(stocklist, categories)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, (stocklist, categories), result, expected))
                self.assertEqual(result, expected, msg)
            print "Solution '{}' passed all tests!".format(name)


if __name__ == '__main__':
    unittest.main()
