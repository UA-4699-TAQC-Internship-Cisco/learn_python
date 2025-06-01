import unittest
from codewars import IMPLEMENTATIONS


class TestZeros(unittest.TestCase):
    test_cases = [
        (0, 0),
        (6, 1),
        (14, 2),
        (25, 6),
        (30, 7),
        (5, 1),
        (4, 0),
        (-1, 0)
    ]

    def run_assertions(self, func, cases, name):
        for inp, expected in cases:
            result = func(inp)
            msg = "[%s] In: %s, Got: %s, Exp: %s" % (name, inp, result, expected)
            self.assertEqual(result, expected, msg)

    def test_all_implementations_zeros(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "zeros"):
                print "Testing solution for zeros:", name
                zeros_func = kyu["kyu5"].zeros
                self.run_assertions(zeros_func, self.test_cases, name)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for zeros:", name


if __name__ == '__main__':
    unittest.main()
