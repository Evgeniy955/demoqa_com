from hamcrest import assert_that, equal_to

from conftest import driver
from testlib.locators import text_box
from testlib.locators.text_box import check_send_form
from tests.base_page import BasePage
from utils.generator.generator import generated_person_for_text_box

list_of_field = ["full_name", "email", "current_address", "permanent_address"]


class TextBox(BasePage):

    @classmethod
    def fill_text_fields_and_submit(cls, driver, session):
        person_for_text_box = generated_person_for_text_box()
        session["full_name"] = person_for_text_box.full_name
        cls.find_current_element(driver, text_box.FULL_NAME).send_keys(session["full_name"])
        session["email"] = person_for_text_box.email
        cls.find_current_element(driver, text_box.EMAIL).send_keys(session["email"])
        session["current_address"] = person_for_text_box.current_address
        cls.find_current_element(driver, text_box.CURRENT_ADDRESS).send_keys(session["current_address"])
        session["permanent_address"] = person_for_text_box.permanent_address
        cls.find_current_element(driver, text_box.PERMANENT_ADDRESS).send_keys(session["permanent_address"])
        submit_button = cls.find_current_element(driver, text_box.SUBMIT)
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        cls.find_current_element(driver, text_box.SUBMIT).click()

    @classmethod
    def check_form(cls, driver, session):
        text_dict = {
            "full_name": "Name:",
            "email": "Email:",
            "current_address": "Current Address :",
            "permanent_address": "Permananet Address :"
        }
        index = 1
        for _ in range(4):
            text = cls.find_current_element(driver, check_send_form(index)).text
            if text.split(":")[0] in ["Current Address ", "Permananet Address "]:
                assert_that(text, equal_to(
                    text_dict[list_of_field[index - 1]] + session[list_of_field[index - 1]].replace("\n", " ")))
            else:
                assert_that(text, equal_to(text_dict[list_of_field[index - 1]] + session[list_of_field[index - 1]]))
            index += 1

    @classmethod
    def check_placeholders(cls, driver):
        placeholders = ['Full Name', 'name@example.com', 'Current Address']
        assert_that(cls.find_current_element(driver, text_box.FULL_NAME).get_attribute("placeholder"),
                    equal_to(placeholders[0]))
        assert_that(cls.find_current_element(driver, text_box.EMAIL).get_attribute("placeholder"),
                    equal_to(placeholders[1]))
        assert_that(cls.find_current_element(driver, text_box.CURRENT_ADDRESS).get_attribute("placeholder"),
                    equal_to(placeholders[2]))
