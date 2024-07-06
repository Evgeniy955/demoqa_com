import os

from selenium.webdriver import Keys

from testlib.locators import practice_form_locators
from tests.base_page import BasePage
from utils.generator.generator import generated_person, generated_file


class FormPage(BasePage):

    @classmethod
    def fill_fields_and_submit(cls, driver):
        person = generated_person()
        path = generated_file()
        cls.remove_footer(driver)
        cls.find_current_element(driver, practice_form_locators.FIRST_NAME).send_keys(person.first_name)
        cls.find_current_element(driver, practice_form_locators.LAST_NAME).send_keys(person.last_name)
        cls.find_current_element(driver, practice_form_locators.EMAIL).send_keys(person.email)
        cls.find_current_element(driver, practice_form_locators.GANDER).click()
        cls.find_current_element(driver, practice_form_locators.MOBILE).send_keys(person.mobile)
        subject = cls.find_current_element(driver, practice_form_locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        cls.find_current_element(driver, practice_form_locators.HOBBIES).click()
        cls.find_current_element(driver, practice_form_locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        cls.find_current_element(driver, practice_form_locators.CURRENT_ADDRESS).send_keys(person.current_address)
        cls.find_current_element(driver, practice_form_locators.SUBMIT).click()
        return person

    @classmethod
    def form_result(cls, driver):
        result_list = cls.find_current_elements(driver, practice_form_locators.RESULT_TABLE)
        result_text = [el.text for el in result_list]
        return result_text

    @classmethod
    def check_field_name_of_practice_form(cls, driver):
        label_names = {
            "labels": ["Name", "Email", "Mobile(10 Digits)", "Date of Birth", "Subjects", "Hobbies",
                       "Picture",
                       "Current Address", "State and City"],
        }
        locator = {"labels": practice_form_locators.LABELS_TEXT}
        assert cls.find_current_element(driver,
                                        practice_form_locators.HEADER_TEXT_BOX).text == "Practice Form", "Wrong header text"
        assert cls.find_current_element(driver,
                                        practice_form_locators.SUB_TITLE_TEXT_BOX).text == "Student Registration Form", "Wrong title text"
        assert cls.find_current_element(driver,
                                        practice_form_locators.GANDER_TEXT).text == "Gender", "Wrong header text"
        cls.check_block_elements(driver, label_names, locator)

    @classmethod
    def check_button_and_checkbox_names(cls, driver):
        dict_names = {
            "button_names": ["Male", "Female", "Other"],
            "checkbox_names": ["Sports", "Reading", "Music"]
        }
        locator = {"button_names": practice_form_locators.RADIO_BUTTONS_TEXT,
                   "checkbox_names": practice_form_locators.CHECKBOX_TEXT}
        cls.check_block_elements(driver, dict_names, locator)

    @classmethod
    def fail_test(cls, driver):
        dict_names = {
            "button_names": ["Males", "Femalse", "Othser"],
            "checkbox_names": ["Sporats", "Readinsg", "Msusic"]
        }
        locator = {"button_names": practice_form_locators.RADIO_BUTTONS_TEXT,
                   "checkbox_names": practice_form_locators.CHECKBOX_TEXT}
        cls.check_block_elements(driver, dict_names, locator)
