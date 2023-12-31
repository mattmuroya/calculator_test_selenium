# calculator_test_selenium

This repository contains a basic Python/Selenium WebDriver UI test automation
framework that does not depend on a preexisting test framework library (e.g.
Pytest). The sample tests use this
[online calculator application](https://testsheepnz.github.io/BasicCalculator.html),
however you can test any web page by creating page objects/interaction methods
in the `Pages` directory.

This document includes a quick start guide as well as a brief functional
description of each framework component.

## Quick Start

You must have Python installed to execute test suite. To run the suite on your
local machine:

1. Clone (or download) this repository.

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
   $ python calculator_tests.py
   ```

The console prints individual results as tests finish executing. After all tests
have been executed, the console prints a final count of the passed test cases.

## Framework Design Documentation

This framework prioritizes modularity and extensibility. It is based on the Page
Object Model (POM) design pattern.

```
calculator_test_selenium/
├─ pages/
│  ├─ calculator_page.py
│  ├─ page_2.py
│  ├─ page_3.py
│  └─ [...].py
├─ utils/
│  ├─ output_py
│  ├─ test_runner.py
│  └─ webdriver.py
├─ calculator_tests.py
├─ suite_2_tests.py
├─ suite_3_tests.py
└─ [...].py
```

### Pages

Each file in the `pages` directory contains a class representing a web page to
be tested. The class contains all of the element locators and interaction
methods (WebDriver calls) for that page. The actual test scripts will call these
methods to interact with elements on the webpage.

The sample page file `calculator_page.py` contains the `CalculatorPage` class
which represents
[this online calculator application](https://testsheepnz.github.io/BasicCalculator.html).
It contains methods for loading the url, entering values into the number fields,
executing calculations, retrieving the contents of the result field, and reading
the error message banner.

As your application/test suite grows, you can add new pages to the directory and
define new element locators/interaction methods for existing pages.

### Test Suites

Test suite files contain the actual test scripts and are placed in the root
directory. Each test suite imports one or more page object classes from the
`pages` directory, then uses the interaction methods from that page to define
the test cases. Each test case can be executed multiple times with different
browsers and/or parameters (defined at the bottom file).

The sample test suite `calculator_tests.py` imports the `CalculatorPage` page
and defines just one test `test_calculator_operations`. To include a test
definition in the actual script execution, add it to the `execute_tests` block
at the bottom of the page along with one or more groups of parameters to run
with that test. When you execute `calculator_tests.py`, the script runs each
test for every group of parameters associated with it.

### Utils

The `utils` directory contains the code for the test runner itself, print
output, and WebDriver configuration. If your tests require mock data, you can
create reusable dependency injection modules in this directory.
