from typing import Type, Dict

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from config.env import BROWSER, get

REMOTE_OPTIONS = get("REMOTE_OPTIONS", "")

browsers: Dict[str, Type[WebDriver]] = {
    "chrome": webdriver.Chrome,
    "edge": webdriver.Edge,
    "firefox": webdriver.Firefox,
    "safari": webdriver.Safari
}

if BROWSER == 'chrome':
    browser_options = webdriver.ChromeOptions()
elif BROWSER == 'firefox':
    browser_options = webdriver.FirefoxOptions()
elif BROWSER == 'edge':
    browser_options = webdriver.EdgeOptions()
elif BROWSER == 'safari':
    browser_options = webdriver.SafariOptions()


class Driver:

    def __init__(self):
        self.options = browser_options

        self.options.add_argument("--window-size=1920,1080")
        # self.options.add_argument("--headless")

        for option in REMOTE_OPTIONS.split():
            self.options.add_argument(option)

    def start(self):
        if BROWSER in ["chrome", "edge", "firefox", 'safari']:
            driver: WebDriver = browsers[BROWSER](options=self.options)
            driver.maximize_window()
        else:
            driver = None
        return driver
