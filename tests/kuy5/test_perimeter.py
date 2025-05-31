import unittest
from codewars import IMPLEMENTATIONS


class TestPerimeterSolutions(unittest.TestCase):
    test_cases = [
        (0, 4),
        (5, 80),
        (7, 216),
        (20, 114624),
        (30, 14098308),
        (100, 6002082144827584333104),
        (500, 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504),
    ]

    def test_all_perimeter(self):
        for name, kyu in IMPLEMENTATIONS.items():
            if "kyu5" in kyu and hasattr(kyu["kyu5"], "perimeter"):
                func = kyu["kyu5"].perimeter
                for input_val, expected in self.test_cases:
                    result = func(input_val)
                    msg = "[{}] input: {}, got: {}, expected: {}".format(name, input_val, result, expected)
                    self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
