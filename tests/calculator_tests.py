"""Test suite for https://testsheepnz.github.io/BasicCalculator.html
"""

# Import page object classes
from pages.calculator_page import CalculatorPage

# ==================== Define test cases ====================

class CalculatorTests:
    """Test suite object class for https://testsheepnz.github.io/BasicCalculator.html
    """
    def test_calculator_operations(self, browser, operation, arg_1, arg_2, expected_result, inputs_valid):
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
        if inputs_valid:
            answer = calculator.get_answer()
            assert answer == expected_result
        else:
            error_message = calculator.get_error_message()
            assert error_message == expected_result

    # def test_case_2():
    #     pass

    # def test_case_3():
    #     pass
