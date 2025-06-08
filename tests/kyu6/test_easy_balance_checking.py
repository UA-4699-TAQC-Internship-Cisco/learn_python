import unittest
from codewars import IMPLEMENTATIONS

class BalanceTest(unittest.TestCase):

    test_data = [
        (
            """1000.00!=
                125 Market !=:125.45
                126 Hardware =34.95
                127 Video! 7.45
                128 Book :14.32
                129 Gasoline ::16.10
                """,
            """Original Balance: 1000.00\r
                125 Market 125.45 Balance 874.55\r
                126 Hardware 34.95 Balance 839.60\r
                127 Video 7.45 Balance 832.15\r
                128 Book 14.32 Balance 817.83\r
                129 Gasoline 16.10 Balance 801.73\r
                Total expense  198.27\r
                Average expense  39.65"""
        ),
        (
            """1233.00
                125 Hardware;! 24.8?;
                123 Flowers 93.5
                127 Meat 120.90
                120 Picture 34.00
                124 Gasoline 11.00
                123 Photos;! 71.4?;
                122 Picture 93.5
                132 Tyres;! 19.00,?;
                129 Stamps 13.6
                129 Fruits{} 17.6
                129 Market;! 128.00?;
                121 Gasoline;! 13.6?;""",
            """Original Balance: 1233.00\r
                125 Hardware 24.80 Balance 1208.20\r
                123 Flowers 93.50 Balance 1114.70\r
                127 Meat 120.90 Balance 993.80\r
                120 Picture 34.00 Balance 959.80\r
                124 Gasoline 11.00 Balance 948.80\r
                123 Photos 71.40 Balance 877.40\r
                122 Picture 93.50 Balance 783.90\r
                132 Tyres 19.00 Balance 764.90\r
                129 Stamps 13.60 Balance 751.30\r
                129 Fruits 17.60 Balance 733.70\r
                129 Market 128.00 Balance 605.70\r
                121 Gasoline 13.60 Balance 592.10\r
                Total expense  640.90\r
                Average expense  53.41"""
        )
    ]

    def test_balance_equal(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for actual, expected in self.test_data:
                result = kyu["kyu6"].balance(actual)
                self.assertEqual(result, expected)
            print "Solution '{}' passed  test!".format(name)


    def test_balance_not_equal(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for actual, expected in self.test_data:
                result = kyu["kyu6"].balance(actual)
                self.assertNotEqual(result, expected)
            print "Solution '{}' passed  test!".format(name)

    def test_balance_returns_string(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for elem in self.test_data:
                result = kyu["kyu6"].balance(elem[0])
                self.assertIsInstance(result, str)
            print "Solution '{}' passed  test!".format(name)

    def test_keywords_in_balance(self):
        expected_word = ["Original Balance", "Total expense", "Average expense"]
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            for elem in self.test_data:
                result = kyu["kyu6"].balance(elem[0])
                for word in expected_word:
                    self.assertIn(word, result)
            print "Solution '{}' passed  test!".format(name)


    def test_with_wrong_input_type(self):
        for name, kyu in IMPLEMENTATIONS.items():
            print "\nTesting solution: {}".format(name)
            with self.assertRaises(TypeError):
                kyu["kyu6"].balance(123)
            print "\nTesting solution: {}".format(name)
