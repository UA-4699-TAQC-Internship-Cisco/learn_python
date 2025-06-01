import unittest
from codewars import IMPLEMENTATIONS

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
        for  name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for actual, expected in self.test_data:
                result = kyu["kyu8"].count_positives_sum_negatives(actual)
                self.assertEqual(result, expected)
            print "Solution '{}' passed  test!".format(name)

    def test_count_positives_return_list(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            result = kyu["kyu8"].count_positives_sum_negatives([])
            self.assertIsInstance(result, list)
            print "Solution '{}' passed  test!".format(name)

    def test_with_wrong_input_type(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            with self.assertRaises(TypeError):
                kyu["kyu8"].count_positives_sum_negatives("wrong test_data type")
            print "\nTesting solution: {}".format(name)
