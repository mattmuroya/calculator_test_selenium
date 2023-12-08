"""Define and execute test cases and parameters (test data) for the Calculator app.
"""

# Import test utilities
from utils.webdriver import create_driver
from utils.test_runner import execute_tests

# Import page object classes
from pages.calculator import CalculatorPage

# ==================== Define test cases ====================

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

# def test_case_2():
#     pass

# def test_case_3():
#     pass

# ========== Define parameter sets and execute test suite ==========

if __name__ == "__main__":
    execute_tests([
        (test_calculator_operations, [
            ("Add", "15", "30", "45", True),
            ("Add", "5", "Five", "Number 2 is not a number", False),
            # ("Subtract", "15", "40", "-25", True),
            # ("Multiply", "8", "8", "64", True),
            # ("Divide", "12", "3", "4", True),
            # ("Concatenate", "12", "34", "1234", True),
        ]),
        # (test_case_2, [
        #     (),
        #     (),
        #     (),
        # ]),
        # (test_case_2, [
        #     (),
        #     (),
        #     (),
        # ]),
    ])
