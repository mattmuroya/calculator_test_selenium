"""Defines functions used for executing test case suites.
"""

from utils.output import print_test_begin, print_test_end

def execute_test_case(test, param_sets):
    """Takes a test definition, a list of parameter sets, and passed/total
    counters and executes the test for each set of data in the params list,
    incrementing the passed/total counters each time.
    """
    passed = 0
    total = 0

    for param_set in param_sets:
        try:
            test(*param_set)
            passed += 1
            print("✅ PASS:", test.__name__)
        except AssertionError:
            print("❌ FAIL:", test.__name__, param_set)
        total +=1

    return (passed, total)

def execute_tests(test_cases):
    """Takes a list of tuples, each of which contains a test case and list of
    parameter sets, and executes each pair in sequence.
    """
    passed = 0
    total = 0

    print_test_begin()

    for test_case in test_cases:
        d_passed, d_total = execute_test_case(test_case[0], test_case[1])
        passed += d_passed
        total += d_total

    print_test_end(passed, total)
