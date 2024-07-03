from typing import Tuple

from selenium.webdriver.common.by import By
from random import randint

from conftest import driver
from testlib.locators.locators_by import css_selector, xpath

HEADER_TEXT_BOX: Tuple = xpath("//h1[contains(@class, 'text-center')]")
BUTTON_TO_SEE_ALERT: Tuple = xpath('//span[text()="Click Button to see alert "]')
ALERT_WILL_APPEAR_AFTER_5_SECONDS: Tuple = xpath('//span[text()="On button click, alert will appear after 5 seconds "]')
CONFIRM_BOX: Tuple = xpath('//span[text()="On button click, confirm box will appear"]')
PROMPT_BOX: Tuple = xpath('//span[text()="On button click, prompt box will appear"]')
ALERT_BUTTON: Tuple = css_selector('#alertButton')
TIMER_ALERT_BUTTON: Tuple = css_selector('#timerAlertButton')
CONFIRM_BUTTON: Tuple = css_selector('#confirmButton')
PROMPT_BUTTON: Tuple = css_selector('#promtButton')
CONFIRM_RESULT: Tuple = css_selector('#confirmResult')
PROMPT_RESULT: Tuple = css_selector('#promptResult')
