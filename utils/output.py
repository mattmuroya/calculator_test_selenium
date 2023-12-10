"""Functions for printing test results to the console.
"""

def print_test_begin():
    """Prints BEGINNING TEST EXECUTION banner.
    """
    print("\n============== BEGINNING TEST EXECUTION ===============\n")

def print_pass(test, param_set):
    """Prints test name and parameter set for a passed test case.
    """
    print("✅ PASS:", test.__name__, param_set)

def print_fail(test, param_set):
    """Prints test name and parameter set for a failed test case.
    """
    print("❌ FAIL:", test.__name__, param_set)

def print_test_end(passed, total, time):
    """Prints TEST EXECUTION COMPLETE banner with percentage of passed test
    cases and total execution time.
    """
    if total > 0:
        percent = format(passed / total, ".0%")
        print(f"\n===== TEST EXECUTION COMPLETE: {passed} / {total} ({percent}) in {time} =====\n")
    else:
        print("\n===== TEST EXECUTION COMPLETE: NO TESTS FOUND =====\n")
