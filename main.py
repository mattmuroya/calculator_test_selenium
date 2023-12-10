"""Main test suite execution script.
"""

# Import test utilities
from utils.test_runner import execute_tests

# Import test suites
from tests.calculator_tests import CalculatorTests

# ========== Define parameter groups and execute test suites ==========

if __name__ == "__main__":
    calculator_tests = CalculatorTests()
    execute_tests([
        (calculator_tests.test_calculator_operations, [
            ("Chrome", "Add", "15", "30", "45", True),
            ("Chrome", "Add", "5", "Five", "Number 2 is not a number", False),
            # ("Chrome", "Subtract", "15", "40", "-25", True),
            # ("Chrome", "Multiply", "8", "8", "64", True),
            # ("Chrome", "Divide", "12", "3", "4", True),
            # ("Chrome", "Concatenate", "12", "34", "1234", True),
        ]),
        # (test_case_2, [
        #     (),
        #     (),
        #     (),
        # ]),
        # (test_case_3, [
        #     (),
        #     (),
        #     (),
        # ]),
    ])
