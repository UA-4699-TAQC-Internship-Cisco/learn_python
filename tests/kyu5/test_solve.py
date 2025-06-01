import unittest
from codewars import IMPLEMENTATIONS


class TestSolve(unittest.TestCase):
    test_cases = [
        (2.0, 0.5),
        (1.0, 0.38196601125),
        (0.5, 0.267949192431),
        (10.0, 0.729843788129),
        (0.0, 0.0),
        (-1.0, 0.0)
    ]

    def test_all_implementations_solve(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "solve"):
                print "Testing solution for solve:", name
                solve_func = kyu["kyu5"].solve
                for value, expected in self.test_cases:
                    result = solve_func(value)
                    msg = "[%s] In: %s, Got: %s, Exp: %s" % (
                        name, value, result, expected)
                    self.assertAlmostEqual(result, expected, places=10, msg=msg)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for solve:", name


if __name__ == '__main__':
    unittest.main()
