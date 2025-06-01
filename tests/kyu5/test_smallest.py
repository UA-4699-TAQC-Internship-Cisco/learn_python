import unittest
from codewars import IMPLEMENTATIONS


class TestSmallest(unittest.TestCase):
    test_cases = [
        (261235, [126235, 2, 0]),
        (209917, [29917, 0, 1]),
        (285365, [238565, 3, 1]),
        (296837, [239687, 4, 1]),
        (1000000, [1, 0, 6]),
        (1, [1, 0, 0]),
        (10, [1, 0, 1]),
        (21, [12, 0, 1]),
        (300, [3, 0, 2])
    ]

    def test_all_implementations_smallest(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "smallest"):
                print "Testing solution for smallest:", name
                smallest_func = kyu["kyu5"].smallest
                for number, expected in self.test_cases:
                    result = smallest_func(number)
                    msg = "[%s] In: %s, Got: %s, Exp: %s" % (
                        name, number, result, expected)
                    self.assertEqual(result, expected, msg)
                print "Solution '%s' passed all tests!" % name
            else:
                print "Skipping solution for smallest:", name


if __name__ == '__main__':
    unittest.main()
