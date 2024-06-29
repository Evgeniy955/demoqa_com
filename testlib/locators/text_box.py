from typing import Tuple

from selenium.webdriver.common.by import By
from random import randint

from conftest import driver
from testlib.locators.locators_by import css_selector, xpath

FULL_NAME: Tuple = css_selector('#userName')
EMAIL: Tuple = css_selector('#userEmail')
CURRENT_ADDRESS: Tuple = css_selector('#currentAddress')
PERMANENT_ADDRESS: Tuple = css_selector('#permanentAddress')
SUBMIT: Tuple = css_selector('#submit')


def check_send_form(index=None):
    return xpath(f"//div[@id='output']//div[contains(@class, 'border')]//p[{index}]")


HEADER_TEXT_BOX = css_selector('h1')
