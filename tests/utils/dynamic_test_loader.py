# -*- coding: utf-8 -*-

import sys
import os

def load_dynamic_tests(config, test_cases, create_testcase_class, globals_dict):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    for func_key, paths in config.items():
        for full_path in paths:
            module_path, attr_name = full_path.rsplit(".", 1)
            user_name = module_path.split(".")[1]
            module = __import__(module_path, fromlist=[attr_name])
            function_ref = getattr(module, attr_name)

            test_class = create_testcase_class(
                user_name, func_key, function_ref, test_cases[func_key]
            )
            globals_dict[test_class.__name__] = test_class
