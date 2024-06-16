import os

from selenium import webdriver

from config import env
from config.env import BROWSER

browsers = {"chrome": webdriver.Chrome, "remote": webdriver.Remote}

EXPORT_RESULT_IN_TESTRAIL = env.get("EXPORT_RESULT_IN_TESTRAIL", True)
RUN_ID = env.get("PLAN_ID", 0)
CREATE_ALLURE_REPORT = env.get("CREATE_ALLURE_REPORT", True)
ALLURE_REPORT_PATH = env.get("ALLURE_REPORT_PATH", os.path.dirname(__file__))
SESSION_RESULT_PATH = env.get("SESSION_RESULT_PATH", os.path.dirname(__file__))


class Driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()

        if BROWSER == "chrome":
            self.options.add_argument("--window-size=1920,1080")
            # self.options.add_argument("--headless")

    def start(self):
        if BROWSER == "chrome":
            driver = browsers[BROWSER](options=self.options)
            # driver.maximize_window()
        else:
            driver = None
        return driver
