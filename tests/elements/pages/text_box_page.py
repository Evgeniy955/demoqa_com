from faker.providers import person

from testlib.locators import text_box
from testlib.locators.text_box import check_send_form
from tests.base_page import BasePage
from utils.generator.generator import generated_person_for_text_box


class TextBox(BasePage):

    def fill_text_fields_and_submit(self):
        person_for_text_box = generated_person_for_text_box()
        self.element_is_visible(text_box.FULL_NAME).send_keys(person_for_text_box.full_name)
        self.element_is_visible(text_box.EMAIL).send_keys(person_for_text_box.email)
        self.element_is_visible(text_box.CURRENT_ADDRESS).send_keys(person_for_text_box.current_address)
        self.element_is_visible(text_box.PERMANENT_ADDRESS).send_keys(person_for_text_box.permanent_address)
        self.element_is_visible(text_box.SUBMIT).click()

    def check_form(self):
        index = 0
        for _ in range(5):
            print(check_send_form(index))
            self.element_is_visible(check_send_form(index)).get_attribute()
            index += 1

    def check_placeholders(self):
        # self.element_is_visible(text_box.PERMANENT_ADDRESS).send_keys(person_for_text_box.permanent_address)
        ...
