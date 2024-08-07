from typing import Tuple

from allure import step

from testlib.locators.locators_by import css_selector, xpath

FULL_NAME: Tuple = css_selector('#userName')
# FULL_NAME_LABEL: Tuple = css_selector('#userName-label')
EMAIL: Tuple = css_selector('#userEmail')
# EMAIL_LABEL: Tuple = css_selector('#userEmail-label')
CURRENT_ADDRESS: Tuple = css_selector('#currentAddress')
# CURRENT_ADDRESS_LABEL: Tuple = css_selector('#currentAddress-label')
PERMANENT_ADDRESS: Tuple = css_selector('#permanentAddress')
# PERMANENT_ADDRESS_LABEL: Tuple = css_selector('#permanentAddress-label')
SUBMIT: Tuple = css_selector('#submit')
HEADER_TEXT_BOX: Tuple = xpath("//h1[contains(@class, 'text-center')]")
LABELS_TEXT: Tuple = xpath('//*[@id="userForm"]//*[contains(@id,"-label")]')


@step('check send form')
def check_send_form(index=None):
    return xpath(f"//div[@id='output']//div[contains(@class, 'border')]//p[{index}]")
