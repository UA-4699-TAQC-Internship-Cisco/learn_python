import unittest
from codewars import IMPLEMENTATIONS


class TestIsPrime(unittest.TestCase):
    test_cases = [
        (2, True),
        (3, True),
        (7, True),
        (11, True),
        (1, False),
        (0, False),
        (4, False),
        (9, False),
        (10, False),
        (-5, False)
    ]

    def test_all_implementations_is_prime(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "is_prime"):
                print "Testing solution for is_prime:", name
                is_prime_func = kyu["kyu5"].is_prime
                for number, expected in self.test_cases:
                    result = is_prime_func(number)
                    msg = "[%s] In: %s, Got: %s, Exp: %s" % (
                        name, number, result, expected)
                    self.assertEqual(result, expected, msg)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for is_prime:", name


if __name__ == '__main__':
    unittest.main()
