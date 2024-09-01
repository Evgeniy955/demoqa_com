from random import randint
from typing import Tuple

from testlib.locators.locators_by import css_selector, xpath

LAST_NAME: Tuple = css_selector('#lastName')
FIRST_NAME: Tuple = css_selector('#firstName')
EMAIL: Tuple = css_selector('#userEmail')
GANDER: Tuple = css_selector(f"label[for='gender-radio-{randint(1, 3)}']")
MOBILE: Tuple = css_selector('#userNumber')
SUBJECT: Tuple = css_selector('#subjectsInput')
HOBBIES: Tuple = css_selector(f"label[for='hobbies-checkbox-{randint(1, 3)}']")
# CLOSE_BUTTON: Tuple = css_selector('#closeLargeModal')
FILE_INPUT: Tuple = css_selector('#uploadPicture')
CURRENT_ADDRESS: Tuple = css_selector('#currentAddress')
# SUBMIT: Tuple = css_selector('#submit')
SUBMIT: Tuple = xpath('//button[text()="Submit"]')
RESULT_TABLE: Tuple = xpath('//div[@class="table-responsive"]//td[2]')

HEADER_TEXT_BOX: Tuple = xpath("//h1[contains(@class, 'text-center')]")
SUB_TITLE_TEXT_BOX: Tuple = xpath("//h5[contains(text(), 'Form')]")
LABELS_TEXT: Tuple = xpath('//*[@id="userForm"]//*[contains(@id,"-label")]')
RADIO_BUTTONS_TEXT: Tuple = xpath('//label[contains(@for, "gender-radio")]')
CHECKBOX_TEXT: Tuple = xpath('//label[contains(@for, "hobbies-checkbox")]')
GANDER_TEXT: Tuple = xpath('//*[@id="genterWrapper"]//*[ text()="Gender"]')
