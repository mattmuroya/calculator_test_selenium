# calculator_test_selenium

This repository contains a basic Python/Selenium WebDriver UI test automation
framework that does not depend on a preexisting test framework library (e.g.
Pytest). The sample tests use
[this online calculator application](https://testsheepnz.github.io/BasicCalculator.html),
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

5. Execute the main test script:

   ```console
   $ python main.py
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
│  └─ page_3.py
├─ tests/
│  ├─ calculator_tests.py
│  ├─ page_2.py
│  └─ page_3.py
├─ utils/
│  ├─ output_py
│  ├─ test_runner.py
│  └─ webdriver.py
└─ main.py
```

### `main.py`

`main.py` is the main test execution script. This file defines which test suites
(and which tests cases from each of those suites) are run. This file also
defines the parameter groups (data sets) to be run with each test case. Each
test case will execute once for every parameter group defined for it in the
`execute_tests` block in this file.

### Pages

Each file in the `pages` directory contains an object class that represents a
web page to be tested. The class contains all of the individual element locators
and interaction methods (WebDriver calls) for that page.

The sample page file `calculator_page.py` contains the `CalculatorPage` class
which represents
[this online calculator application](https://testsheepnz.github.io/BasicCalculator.html).
It contains methods for loading the url, entering values into the number fields,
executing calculations, retrieving the contents of the result field, and reading
the error message banner.

You can add new pages to the directory and define new element
locators/interaction methods for existing pages.

### Tests

Each file in the `tests` directory contains an object class that represents a
test suite comprising related test case definitions (methods). Each test suite
imports one or more page object classes from the `pages` directory, and the test
case definitions use methods from the page object to script out the actual test
steps.

The sample test suite `calculator_tests.py` imports the `CalculatorPage` class
and uses the page interaction methods to define the one test `test_operations`
test case definition.

You can reuse the page interaction methods to create new test cases and modify
the existing tests.

### Utils

The `utils` directory contains the code for the test runner itself, print
output, and WebDriver configuration. If your tests require mock data, you can
create reusable dependency injection modules in this directory.
