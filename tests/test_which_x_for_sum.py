import unittest
from codewars.TYakushevych import ky5 as test_sum

class TestWhichXForSum(unittest.TestCase):

    test_data = [
        (2.00, 5.000000000000e-01),
        (4.00, 6.096117967978e-01),
        (5.00, 6.417424305044e-01),
        (6.00, 6.666666666667e-01)
    ]

    def test_sum_is_for_x_equal(self):
        for actual, expected in self.test_data:
            result = test_sum.solve(actual)
            self.assertAlmostEqual(result, expected)

    def test_sum_is_for_x_returns_float(self):
        self.assertIsInstance(test_sum.solve(5.0), float)

    def test_sum_is_for_x_abs_difference_less_than_expected(self):
        exponent = 1e-12
        for actual, expected in self.test_data:
            result = abs(test_sum.solve(actual) - expected)
            self.assertLessEqual(result, exponent)  #check that abs(actual - expected) <= 1e-12


