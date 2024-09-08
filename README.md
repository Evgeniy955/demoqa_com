# The project is created on pure selenium and python+pytest

### The resource was used to write the project:

- https://demoqa.com/
- CI/CD - Github actions

## The project includes:

### 1. Added a custom module pytest-cmdline-add-args 1.9.5

    - The module allows you to change the command line arguments for running tests.
    - The module allows you to change the command line arguments for getting allure reports. 
    - A custom method for loading system requests with the env.py file has been added to the module, 
    which allows you to manage the module from the project itself.

https://pypi.org/project/pytest-cmdline-add-args/

### 2. The project is cross-browser

#### 1. Locally:

    - On Windows, tests work for Chrome, Edge, Firefox
    - On Mac OS, tests work for Chrome, Edge, Safari

#### 2. Tests only work remotely for Chrome and Edge

    - With Firefox problems, because there are some conflicts when installing the browser in Ubuntu

### 3. Allur reports

1. #### Locally:
    - You need to specify in the config/env.py file:
        * CREATE_ALLURE_REPORT = True
    - If CREATE_ALLURE_REPORT = True:
        * The allure report will automatically open in the browser

#### 2. Удаленно:

    - During automatic runs, reports are create automatically

3. #### Sending allure reports
    - When running automatically, reports are sent automatically.
    - When running manually, you can specify whether to run a send report or not (locally and remotely):
        * For local sending, you need to create a .env file and specify the data for the report to email

### 4. Running tests via GitHub actions

If you are going to run tests using GitHub actions, you need to specify the name of your project in workflow:

env:
#### PROJECT_NAME: project_name

#### 1. Customizing test execution

    - You can select the resource section for which the tests will be run 
    - You can select the browser for running the tests 
    - You can choose whether to send the report by email or not

#### 2. allure report to the resource is deploying in https://evgeniy955.github.io/demoqa_com/

    - Displays all tests that have been run for this project.
    - Saves run history for each test.
    - Saves retries history for each test.

### 5. Running tests locally

#### 1. Customizing test execution

    - You can run a specific test, 
        eg. -m "C0007" 
    - You can run tests for any section of the project 
    - You can specify a browser to run tests 
    - You can turn it on  or turn it off to create an allure report 
    - You can turn on or turn off to send an allure report by email

#### 2. The local run  tests setting is set in the file config/env.py