# calculator_test_selenium

This repository contains a basic Python/Selenium WebDriver UI test automation
suite for a
[basic online calculator application](https://testsheepnz.github.io/BasicCalculator.html)
without using a testing framework library such as Pytest.

This document includes a quick start guide as well as a brief technical
description of the main repository components.

## Quick Start Guide

You must have Python installed to execute this test suite. To run the suite on
your local machine:

1. Clone (or download) this repository to your local machine.

   ```console
   $ git clone https://github.com/mattmuroya/calculator_test_selenium.git
   ```

2. Change directory into the repository.

   ```console
   $ cd calculator_test_selenium
   ```

3. Optionally, create and activate a virtual environment.

   ```console
   $ python -m venv venv
   ```

   Activate on Windows:

   ```console
   $ .\venv\Scripts\activate
   ```

   Activate on MacOS/Linux:

   ```console
   $ source venv/bin/activate
   ```

4. Install the required dependencies.

   ```console
   $ pip -r requirements.txt
   ```

5. Execute the test suite:

   ```console
   $ python test_calculator.py
   ```

The test suite and included base test cases will execute. You should see a print
line with the result of each test and a final test summary.

## Framework Design Documentation

This suite is loosely based on the Page Object Model (POM) design pattern. The
main script is contained in `test_calculator.py` which includes the test case
definitions, test data, and executions. The actual WebDriver initialization,
page interactions, and output are handled separately.

### Pages

Each file in the `pages` directory contains at least one class that represents a
specific web page to be tested. The class contains all of the element locators,
WebDriver calls, and interaction methods for that page.

For example, the `calculator.py` file contains a class called `CalculatorPage`
that contains a `url` class variable
(https://testsheepnz.github.io/BasicCalculator.html) and various methods for
interacting with and retrieving data from the elements on that page, such as
loading the url, entering/executing a basic calculation, and checking the
results or error message fields.

As your application/test suite grows, you can add new pages/classes and
WebDriver calls/page interaction methods. These pages and their interaction
methods will be called by individual test cases at execution time.

### Utils

The `utils` directory contains two modules - one for initializing and
configuring the WebDriver object, and another for handling the print output.

#### driver.py

`driver.py` handles the creation and configration of the WebDriver object.
Keeping the driver in its own module allows for reusability across multiple test
suites, as well as the option for exapanding its configuration options in the
future to allow for greater control over things like what browser to use for
each test case.

#### output.py

`output.py` is a small utility that handles test execution print output and can
be reused between suites.
