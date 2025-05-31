import unittest

from codewars import IMPLEMENTATIONS


class TestStockListSolutions(unittest.TestCase):
    test_cases = [
        ((["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], ["A", "B", "C", "W"]),
         "(A : 20) - (B : 114) - (C : 50) - (W : 0)"),
        ((["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]),
         "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"),
        ((["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]),
         "(A : 200) - (B : 1140)")
    ]

    def test_all_stock_list(self):
        for name, kyu in IMPLEMENTATIONS.items():
            for (stocklist, categories), expected in self.test_cases:
                result = kyu["kyu6"].stock_list(stocklist, categories)
                msg = ("[{}] input: {}, got: {}, expected: {}"
                       .format(name, (stocklist, categories), result, expected))
                self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
