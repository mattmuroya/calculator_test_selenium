"""Page object class for https://testsheepnz.github.io/BasicCalculator.html
"""

# Import Selenium WebDriver methods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CalculatorPage:
    """Defines element locators and page interaction methods for the Basic
    Calculator app.
    """
    # =============== Initialization / class variables ===============

    url = "https://testsheepnz.github.io/BasicCalculator.html"

    # Element locators

    number_1_field = (By.ID, "number1Field")
    number_2_field = (By.ID, "number2Field")
    operation_dropdown = (By.ID, "selectOperationDropdown")
    calculate_button = (By.ID, "calculateButton")
    answer_field = (By.ID, "numberAnswerField")
    error_message_field = (By.ID, "errorMsgField")

    # Initializer

    def __init__(self, driver):
        self.driver = driver

    # ==================== Page interaction methods ====================

    def load(self):
        """Loads the page URL.
        """
        self.driver.get(self.url)

    # Input methods

    def enter_first_number(self, text):
        """Enters a text value into the 'First number' field.
        """
        field = self.driver.find_element(*self.number_1_field)
        field.send_keys(text)

    def enter_second_number(self, text):
        """Enters a text value into the 'Second number' field.
        """
        field = self.driver.find_element(*self.number_2_field)
        field.send_keys(text)

    def set_operation_dropdown(self, operation):
        """Sets the Operation dropdown to the specified text value.
        """
        dropdown = Select(self.driver.find_element(*self.operation_dropdown))
        dropdown.select_by_visible_text(operation)

    def click_calculate_button(self):
        """Clicks the Calculate button.
        """
        calc_btn = self.driver.find_element(*self.calculate_button)
        calc_btn.click()

    # Read methods

    def get_answer(self):
        """Returns the text value of the Answer field.
        """
        answer = self.driver.find_element(*self.answer_field)
        return answer.get_attribute('value')

    def get_error_message(self):
        """Reads and returns the text value of the error message banner.
        """
        error_message = self.driver.find_element(*self.error_message_field)
        return error_message.text
