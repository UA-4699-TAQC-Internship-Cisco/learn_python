import unittest
from codewars import IMPLEMENTATIONS


class TestPerimeter(unittest.TestCase):
    test_cases = [
        (0, 4),
        (1, 8),
        (5, 80),
        (7, 216)
    ]

    def test_all_implementations_perimeter(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "perimeter"):
                print "Testing solution for perimeter:", name
                perimeter_func = kyu["kyu5"].perimeter
                for number, expected in self.test_cases:
                    result = perimeter_func(number)
                    msg = "[%s] In: %s, Got: %s, Exp: %s" % (
                        name, number, result, expected)
                    self.assertEqual(result, expected, msg)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for perimeter:", name


if __name__ == '__main__':
    unittest.main()
