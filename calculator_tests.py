"""Test suite for https://testsheepnz.github.io/BasicCalculator.html
"""

# Import test utilities
from utils.test_runner import execute_tests

# Import page object classes
from pages.calculator_page import CalculatorPage

# ==================== Define test cases ====================

def test_calculator_operations(browser, operation, arg_1, arg_2, expected_result, inputs_are_valid):
    """Executes a basic calculator operation with two valid or invalid inputs
    and verifies the result.
    """
    # Initialize page object
    calculator = CalculatorPage(browser)

    # Execute test steps
    calculator.load()
    calculator.set_operation_dropdown(operation)
    calculator.enter_first_number(arg_1)
    calculator.enter_second_number(arg_2)
    calculator.click_calculate_button()

    # Assert results
    if inputs_are_valid:
        answer = calculator.get_answer()
        assert answer == expected_result
    else:
        error_message = calculator.get_error_message()
        assert error_message == expected_result

# def test_case_2(browser):
#     pass

# def test_case_3(browser):
#     pass

# ========== Define parameter groups and execute test suite ==========

if __name__ == "__main__":
    execute_tests([
        [test_calculator_operations, [
            ["Chrome", "Add", "15", "30", "45", True],
            ["Chrome", "Add", "5", "Five", "Number 2 is not a number", False],
            # ["Chrome", "Subtract", "15", "40", "-25", True],
            # ["Chrome", "Multiply", "8", "8", "64", True],
            # ["Chrome", "Divide", "12", "3", "4", True],
            # ["Chrome", "Concatenate", "12", "34", "1234", True],
        ]],
        # [test_case_2, [
        #     ["Chrome"],
        #     ["Firefox"],
        #     ["Edge"],
        # ]],
        # (test_case_3, [
        #     ["Chrome"],
        #     ["Firefox"],
        #     ["Edge"],
        # ]),
    ])
