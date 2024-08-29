from time import sleep

import pytest
import selenium
from selenium.common.exceptions import WebDriverException

from allure_env import get_environment
from config import driver as driver_setup


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


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish():
    get_environment()
    # open allure report. Local only
    # os.popen(f'allure serve {folder_path}')
