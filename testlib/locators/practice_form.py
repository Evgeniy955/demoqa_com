from typing import Tuple

from selenium.webdriver.common.by import By
from random import randint

from testlib.locators.locators_by import css_selector, xpath

LAST_NAME: Tuple = css_selector('#lastName')
FIRST_NAME: Tuple = css_selector('#firstName')
EMAIL: Tuple = css_selector('#userEmail')
GANDER: Tuple = css_selector(f"label[for='gender-radio-{randint(1, 3)}']")
MOBILE: Tuple = css_selector('#userNumber')
SUBJECT: Tuple = css_selector('#subjectsInput')
HOBBIES: Tuple = css_selector(f"label[for='hobbies-checkbox-{randint(1, 3)}']")
FILE_INPUT: Tuple = css_selector('#uploadPicture')
CURRENT_ADDRESS: Tuple = css_selector('#currentAddress')
SUBMIT: Tuple = css_selector('#submit')
RESULT_TABLE: Tuple = xpath('//div[@class="table-responsive"]//td[2]')
