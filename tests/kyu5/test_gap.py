import unittest
from codewars import IMPLEMENTATIONS


class TestGap(unittest.TestCase):
    test_cases = [
        ((2, 100, 110), [101, 103]),
        ((4, 100, 110), [103, 107]),
        ((6, 100, 110), None),
        ((2, 5, 5), None),
        ((4, 2, 3), None),
        ((2, 10, 100), [11, 13])
    ]

    def test_all_implementations_gap(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "gap"):
                print "Testing solution for gap:", name
                gap_func = kyu["kyu5"].gap
                for (gap_value, value, number), expected in self.test_cases:
                    result = gap_func(gap_value, value, number)
                    msg = "[%s] g=%s, r=[%s-%s], Got: %s, Exp: %s" % (
                        name, gap_value, value, number, result, expected)
                    self.assertEqual(result, expected, msg)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for gap:", name


if __name__ == '__main__':
    unittest.main()
