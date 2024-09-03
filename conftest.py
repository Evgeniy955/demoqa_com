import os
from time import sleep

import pytest
import selenium
from selenium.common.exceptions import WebDriverException

from admin.allure_env import get_environment, get_os_type, folder_path
from admin.send_email import send_report_to_email
from config import driver as driver_setup
from config.env import CREATE_ALLURE_REPORT, LOCAL_RUN


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
    if CREATE_ALLURE_REPORT:
        get_environment()
        send_report_to_email()
        if LOCAL_RUN:
            # open allure report. Local only
            print('local run true')
            os.popen(f'allure serve {folder_path}')
