"""Functions for executing test suites and test cases.
"""

from time import time
from datetime import timedelta
from utils import output

def execute_test_case(test, param_sets):
    """Takes a test definition with a list of parameter sets and executes the
    test once for each set. Returns the number of passed/total executions.
    """
    # Initialize counters
    passed = 0
    total = 0

    # Execute test for each parameter set, increment counters
    for param_set in param_sets:
        try:
            test(*param_set)
            passed += 1
            output.print_pass(test, param_set)
        except AssertionError:
            output.print_fail(test, param_set)
        total +=1

    # Return number of passed/total executions
    return (passed, total)

def execute_tests(test_cases):
    """Takes a list of test cases (test definition with a list of parameter
    sets) and executes each test definition/parameter set pairing in sequence.
    """
    # Initialize counters
    passed = 0
    total = 0

    # Begin test suite execution and log start time
    output.print_test_begin()
    t0 = time()

    # Execute each test definition and increment passed/total execution counts.
    for test_case in test_cases:
        p_increment, t_increment = execute_test_case(test_case[0], test_case[1])
        passed += p_increment
        total += t_increment

    # Log end time and report final results
    t1 = time()
    output.print_test_end(passed, total, timedelta(seconds=int(t1-t0)))
