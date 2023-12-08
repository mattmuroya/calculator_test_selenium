"""Page object class for the Calculator app.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CalculatorPage:
    """Page object class for the Calculator app.
    """

    # Class variables

    url = "https://testsheepnz.github.io/BasicCalculator.html"

    # Initializer

    def __init__(self, driver):
        """Takes a driver and initializes the page object
        """
        self._driver = driver

    # Page interaction methods

    def load(self):
        """Loads the page at the class url using the driver
        """
        self._driver.get(self.url)

    def execute_calculation(self, operation, arg_1, arg_2):
        """Takes two arguments and an operation type (Add, Subtract, Multiply,
        Divide, or Concatenate), inputs those values on the page, and executes
        the calculation.
        """
        # Identify page elements
        input_1 = self._driver.find_element(By.ID, "number1Field")
        input_2 = self._driver.find_element(By.ID, "number2Field")
        operation_dropdown = Select(self._driver.find_element(By.ID, "selectOperationDropdown"))
        calculate_button = self._driver.find_element(By.ID, "calculateButton")

        # Execute WebDriver calls
        input_1.send_keys(arg_1)
        input_2.send_keys(arg_2)
        operation_dropdown.select_by_visible_text(operation)
        calculate_button.click()

    def get_result(self):
        """Reads and returns the value in the answer field.
        """
        answer = self._driver.find_element(By.ID, "numberAnswerField")
        return answer.get_attribute('value')

    def get_error_message(self):
        """Reads and returns the in-app error message.
        """
        error = self._driver.find_element(By.ID, "errorMsgField")
        return error.text
