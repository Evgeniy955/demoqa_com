from time import sleep

from conftest import driver
from testlib.locators import alerts_locators
from tests.base_page import BasePage
from utils.generator.generator import generated_person

list_of_fields = ["full_name", "email", "current_address", "permanent_address"]


class Alerts(BasePage):

    @classmethod
    def check_elements_on_alerts_page(cls, driver):
        cls.find_current_element(driver, alerts_locators.HEADER_TEXT_BOX).is_displayed()
        cls.find_current_element(driver, alerts_locators.BUTTON_TO_SEE_ALERT).is_displayed()
        cls.find_current_element(driver, alerts_locators.ALERT_WILL_APPEAR_AFTER_5_SECONDS).is_displayed()
        cls.find_current_element(driver, alerts_locators.CONFIRM_BOX).is_displayed()
        cls.find_current_element(driver, alerts_locators.PROMPT_BOX).is_displayed()
        assert cls.find_current_element(driver, alerts_locators.HEADER_TEXT_BOX).text == "Alerts", (
            "Header name has been changed")
        assert cls.find_current_element(driver, alerts_locators.ALERT_BUTTON).text == "Click me", (
            "Button name has been changed")
        assert cls.find_current_element(driver, alerts_locators.TIMER_ALERT_BUTTON).text == "Click me", ("Button name "
                                                                                                         "has been "
                                                                                                         "changed")
        assert cls.find_current_element(driver, alerts_locators.CONFIRM_BUTTON).text == "Click me", (
            "Button name has been changed")
        assert cls.find_current_element(driver, alerts_locators.PROMPT_BUTTON).text == "Click me", (
            "Button name has been changed")

    @classmethod
    def click_on_alert_button(cls, driver):
        cls.find_current_element(driver, alerts_locators.ALERT_BUTTON).click()
        alert = driver.switch_to.alert
        assert alert.text == "You clicked a button"
        alert.accept()

    @classmethod
    def click_timer_alert_button(cls, driver):
        cls.find_current_element(driver, alerts_locators.TIMER_ALERT_BUTTON).click()
        sleep(5)
        alert = driver.switch_to.alert
        assert alert.text == "This alert appeared after 5 seconds"
        alert.accept()

    @classmethod
    def click_confirm_button(cls, driver):
        cls.find_current_element(driver, alerts_locators.CONFIRM_BUTTON).click()
        alert = driver.switch_to.alert
        assert alert.text == "Do you confirm action?"
        alert.accept()
        assert cls.find_current_element(driver, alerts_locators.CONFIRM_RESULT).text == "You selected Ok"

    @classmethod
    def click_decline_button(cls, driver):
        cls.find_current_element(driver, alerts_locators.CONFIRM_BUTTON).click()
        alert = driver.switch_to.alert
        assert alert.text == "Do you confirm action?"
        alert.dismiss()
        assert cls.find_current_element(driver, alerts_locators.CONFIRM_RESULT).text == "You selected Cancel"

    @classmethod
    def click_prompt(cls, driver):
        person = generated_person()
        cls.find_current_element(driver, alerts_locators.PROMPT_BUTTON).click()
        alert = driver.switch_to.alert
        name = person.first_name
        assert alert.text == "Please enter your name"
        alert.dismiss()
        driver.execute_script("""
                window.promptResponse = arguments[0];
                window.prompt = function() { return window.promptResponse; };
                prompt('Please enter your name:', 'Default name');
            """, name)
        cls.find_current_element(driver, alerts_locators.PROMPT_BUTTON).click()
        assert cls.find_current_element(driver, alerts_locators.PROMPT_RESULT).text == f"You entered {name}"
