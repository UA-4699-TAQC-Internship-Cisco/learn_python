# -*- coding: utf-8 -*-


''' Wilson primes test '''


import unittest
from codewars import IMPLEMENTATIONS


class TestWilsonPrimes(unittest.TestCase):
    ''' wilsons prime (8) kyu8 '''
    # add dir and function path
    functions = [("Dbautista", IMPLEMENTATIONS["Dbautista"]["kyu8"].am_i_wilson),
                 ("YuliaShap", IMPLEMENTATIONS["YuliaShap"]["kyu8"].am_i_wilson),
                 ("BrekhovaT", IMPLEMENTATIONS["BrekhovaT"]["kyu8"].is_wilson_prime)]

    test_cases_positive =  [(0, False),
                            (1, False),
                            (5, True),
                            (6, False),
                            (9, False),
                            (11, False),
                            (13, True),
                            (563, True)
                            ]

    test_cases_negative = [[], {}, "str", 4.8, None]

    def test_with_numbers(self):
        ''' test's body '''
        for name, func in self.functions:
            print u"Testing solution for Wilson Primes: {}".format(name)
            for number, expected in self.test_cases_positive:
                result = func(number)
                msg = ("{} input: {}, got: {}, expected: {}"
                       .format(name, number, result, expected))
                self.assertEqual(result, expected, msg)

    def test_negative_val(self):
        ''' test's body '''
        for name, func in self.functions:
            print u"Testing solution for Wilson Primes: {}".format(name)
            for value in self.test_cases_negative:
                try:
                    result = func(value)
                    print u"Input:", value, "| Output:", result, "| Expected: TypeError"
                except TypeError as e:
                    print u"Input:", value, "| Exception:", type(e).__name__, "-", str(e)



if __name__ == '__main__':
    unittest.main()

