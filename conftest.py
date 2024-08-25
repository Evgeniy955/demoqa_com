from time import sleep

import pytest
import selenium
from selenium.common.exceptions import WebDriverException

from config import driver as driver_setup


# pytest_plugins = ["cmdline_add_args"]


@pytest.fixture()
def driver(session):
    try:
        ui_driver = driver_setup.Driver().start()
    except selenium.common.exceptions.SessionNotCreatedException:
        sleep(1)
        ui_driver = driver_setup.Driver().start()
    session["browser_windows"] = {
        "main_window_handle": ui_driver.current_window_handle,
        "window_handles": ui_driver.window_handles,
    }
    yield ui_driver
    try:
        ui_driver.quit()
    except WebDriverException:
        print("Driver is already closed")


@pytest.fixture(scope="function")
def session():
    return {}

# @pytest.hookimpl(tryfirst=True)
# def pytest_cmdline_preparse(args) -> None:
#     if CREATE_ALLURE_REPORT:
#         new_args = ["-v", f"--alluredir={ALLURE_REPORT_PATH}/allure-results", "--clean-alluredir"]
#         for arg in new_args:
#             if arg not in args:
#                 if args[-1].split(".")[-1] == "py":
#                     args.insert(-1, arg)
#                 else:
#                     args.append(arg)
