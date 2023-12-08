"""WebDriver setup/configuration file.
"""

import selenium.webdriver

def create_driver(browser):
    """Initializes a driver, sets options, and returns the driver object. 
    """

    # Initialize driver
    if browser == "Firefox":
        driver = selenium.webdriver.Firefox()
    elif browser == "Edge":
        driver = selenium.webdriver.Edge()
    else: # Default to Chrome
        driver = selenium.webdriver.Chrome()

    # Configure driver options
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Return driver object
    return driver
