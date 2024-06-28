from typing import Tuple

from selenium.webdriver.common.by import By


def css_selector(locator: str) -> Tuple[str, str]:
    return By.CSS_SELECTOR, locator


def xpath(locator: str) -> Tuple[str, str]:
    return By.XPATH, locator
