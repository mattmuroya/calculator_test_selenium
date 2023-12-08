"""Methods for printing test results.
"""

def print_test_begin():
    print("\n===== BEGINNING TEST EXECUTION =====\n")

def print_test_end(passed, total):
    percent = format(passed /total, ".0%")
    print(f"\n===== TEST EXECUTION COMPLETE: {passed} / {total} ({percent}) PASSED =====\n")
