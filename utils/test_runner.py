"""Functions for executing test suites and test cases.
"""

from time import time
from datetime import timedelta
from utils import output, webdriver

def execute_test_case(test, param_groups):
    """Takes a test definition and a list of parameter groups and executes the
    test once for each group. Returns the number of passed and total executions.
    """
    # Initialize counters
    passed = 0
    executed = 0

    # Create driver and execute test for each parameter group
    for param_group in param_groups:
        driver = webdriver.create_driver(browser=param_group[0])
        try:
            test(driver, *param_group[1:]) # Replace browser name with driver
            output.print_pass(test, param_group)
            passed += 1
        except AssertionError:
            output.print_fail(test, param_group)
        executed +=1
        driver.quit()

    # Return number of passed/total executions
    return (passed, executed)

def execute_tests(test_cases):
    """Takes a list of test cases (test definition with a list of parameter
    groups) and executes each test definition/parameter group pair in sequence.
    """
    # Initialize counters
    total_passed = 0
    total_executed = 0

    # Begin execution and log start time
    output.print_test_begin()
    t0 = time()

    # Execute each test definition and increment passed/total execution counts
    for test_case in test_cases:
        passed, executed = execute_test_case(
            test=test_case[0], param_groups=test_case[1])
        total_passed += passed
        total_executed += executed

    # Log end time and report final results
    t1 = time()
    output.print_test_end(total_passed, total_executed, timedelta(seconds=int(t1-t0)))
