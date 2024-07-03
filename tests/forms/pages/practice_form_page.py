import os

from selenium.webdriver import Keys

from testlib.locators import practice_form_locators, practice_form_locators
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
