"""Functions for printing test results.
"""

def print_test_begin():
    print("\n============== BEGINNING TEST EXECUTION ===============\n")

def print_test_end(passed, total, time):
    if total > 0:
        percent = format(passed / total, ".0%")
        print(f"\n===== TEST EXECUTION COMPLETE: {passed} / {total} ({percent}) in {time} =====\n")
    else:
        print("\n===== TEST EXECUTION COMPLETE: NO TESTS FOUND =====\n")
