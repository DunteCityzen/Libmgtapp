# UNIT TESTS
## PYTEST

I used Pytest module to create tests for this simple application.

You can run the tests while on the application's root directory and virtual environment enabled with the command below

* python -m pytest

There are many options you can use with the python module to customize the test but this generally runs all the tests in the test folder

## Pytest-mocker

I used mocker to simulate interactions with objects without actually modifying them on the application. This was key to ensure the application is not affected by any of the tests we run.

