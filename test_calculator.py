"""Test suite for the Calculator app.
"""

from utils.driver import create_driver
from utils.output import print_test_begin, print_test_end
from pages.calculator import CalculatorPage

# Test cases

def test_calculator_operations(operation, arg_1, arg_2, expected_result, inputs_are_valid):
    """Tests basic calculator operations with valid or invalid inputs.
    """
    # Initialize driver and page object
    driver = create_driver("Chrome")
    calculator = CalculatorPage(driver)

    # Execute test steps
    calculator.load()
    calculator.execute_calculation(operation, arg_1, arg_2)

    # Assert results
    if inputs_are_valid:
        result = calculator.get_result()
        assert result == expected_result
    else:
        error_message = calculator.get_error_message()
        assert error_message == expected_result

    # Quit driver
    driver.quit()

# Test data

test_data_1 = [
    ("Add", "15", "30", "45", True),
    ("Add", "5", "Five", "Number 2 is not a number", False),
    # ("Subtract", "15", "40", "-25", True),
    # ("Multiply", "8", "8", "64", True),
    # ("Divide", "12", "3", "4", True),
    # ("Concatenate", "12", "34", "1234", True),
]

# Execute test suite

if __name__ == "__main__":
    passed = 0
    total = len(test_data_1)

    print_test_begin()

    for data_set in test_data_1:
        try:
            test_calculator_operations(*data_set)
            print("PASS", "Test calculator operations")
            passed += 1
        except AssertionError:
            print("FAIL", "Test calculator operations:", data_set)

    # Insert additional test definitions here

    print_test_end(passed, total)
