from typing import Type, Dict

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from config.env import BROWSER

# EXPORT_RESULT_IN_TESTRAIL = env.get("EXPORT_RESULT_IN_TESTRAIL", True)
# RUN_ID = env.get("PLAN_ID", 0)
# CREATE_ALLURE_REPORT = env.get("CREATE_ALLURE_REPORT", True)
# ALLURE_REPORT_PATH = env.get("ALLURE_REPORT_PATH", os.path.dirname(__file__))
# SESSION_RESULT_PATH = env.get("SESSION_RESULT_PATH", os.path.dirname(__file__))

browsers: Dict[str, Type[WebDriver]] = {
    "chrome": webdriver.Chrome,
    "edge": webdriver.Edge,
    "firefox": webdriver.Firefox,
    "remote": webdriver.Remote
}

if BROWSER == 'chrome':
    browser_options = webdriver.ChromeOptions()
elif BROWSER == 'firefox':
    browser_options = webdriver.FirefoxOptions()
elif BROWSER == 'edge':
    browser_options = webdriver.EdgeOptions()
elif BROWSER == 'remote':
    browser_options = webdriver.ChromeOptions()


class Driver:

    def __init__(self):
        self.options = browser_options

        if BROWSER == "chrome":
            self.options.add_argument("--window-size=1920,1080")
            # self.options.add_argument("--headless")

        elif BROWSER in ["edge", "firefox"]:
            self.options.add_argument("--start-maximized")
            # self.options.add_argument("--headless")

        elif BROWSER == "remote":
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--headless")
            # self.remote_url = "http://selenium:4444/wd/hub"

    def start(self):
        if BROWSER in ["chrome", "edge", "firefox"]:
            driver: WebDriver = browsers[BROWSER](options=self.options)
            # driver.maximize_window()
        elif BROWSER == "remote":
            driver: WebDriver = browsers[BROWSER](options=self.options)
        else:
            driver = None
        return driver
