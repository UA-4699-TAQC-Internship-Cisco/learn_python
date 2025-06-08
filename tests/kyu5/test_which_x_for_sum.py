import unittest
from codewars import IMPLEMENTATIONS

class TestWhichXForSum(unittest.TestCase):

    test_data = [
        (2.00, 5.000000000000e-01),
        (4.00, 6.096117967978e-01),
        (5.00, 6.417424305044e-01),
        (6.00, 6.666666666667e-01)
    ]

    def test_sum_is_for_x_equal(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for actual, expected in self.test_data:
                result = kyu["kyu5"].solve(actual)
                self.assertAlmostEqual(result, expected)
            print "Solution '{}' passed  test!".format(name)

    def test_sum_is_for_x_returns_float(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for elem in self.test_data:
                result = kyu["kyu5"].solve(elem[0])
                self.assertIsInstance(result, float)
            print "Solution '{}' passed  test!".format(name)

    def test_sum_is_for_x_abs_difference_less_than_expected(self):
        exponent = 1e-12
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for actual, expected in self.test_data:
                result = abs(kyu["kyu5"].solve(actual) - expected)
                self.assertLessEqual(result, exponent)  #check that abs(actual - expected) <= 1e-12
            print "Solution '{}' passed  test!".format(name)

    def test_with_wrong_input_type(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            with self.assertRaises(TypeError):
                kyu["kyu5"].solve("wrong test_data type")
            print "\nTesting solution: {}".format(name)