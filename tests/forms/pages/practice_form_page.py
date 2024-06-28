import os

from selenium.webdriver import Keys

from testlib.locators import practice_form
from tests.base_page import BasePage
from utils.generator.generator import generated_person, generated_file


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(practice_form.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(practice_form.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(practice_form.EMAIL).send_keys(person.email)
        self.element_is_visible(practice_form.GANDER).click()
        self.element_is_visible(practice_form.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(practice_form.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(practice_form.HOBBIES).click()
        self.element_is_visible(practice_form.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(practice_form.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(practice_form.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(practice_form.RESULT_TABLE)
        result_text = [el.text for el in result_list]
        return result_text
