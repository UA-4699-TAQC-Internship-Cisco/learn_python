# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
import json
from tests.utils.dynamic_test_loader import load_dynamic_tests

with open("../implementations/ky5.json") as f:
    CONFIG = json.load(f)

TEST_CASES = {
    "gap": [((2, 5, 7), [5, 7]), ((4, 130, 200), [163, 167])],
    "zeros": [((0,), 0), ((6,), 1), ((30,), 7)],
    "perimeter": [((5,), 80), ((7,), 216)],
    "solve": [((2.0,), 0.5), ((6.0,), 2.0 / 3.0)],
    "smallest": [((261235,), [126235, 2, 0]), ((209917,), [29917, 0, 1])]
}

def create_testcase_class(user_id, function_name, func_ref, cases):
    def test_method(self):
        for args, expected in cases:
            if function_name == "solve":
                self.assertAlmostEqual(func_ref(*args), expected, 10)
            else:
                self.assertEqual(func_ref(*args), expected)

    class_name = "Test_{}_{}".format(function_name, user_id)
    return type(class_name, (unittest.TestCase,), {"test_func": test_method})

load_dynamic_tests(CONFIG, TEST_CASES, create_testcase_class, globals())

if __name__ == "__main__":
    unittest.main()
