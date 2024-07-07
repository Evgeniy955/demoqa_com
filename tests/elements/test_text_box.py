from allure import title
from pytest import mark

from tests.elements.pages.text_box_page import TextBox
from utils.helper_methods import test_number


@test_number("01")
@mark.medium_priority
@mark.text_box
@title('check text box form elements')
def test_elements_of_text_box_form(driver, session):
    text_box = TextBox(driver, url='text-box')
    text_box.open()
    text_box.elements_on_text_box_page(driver)
    text_box.check_placeholders(driver)


@test_number("01")
@mark.regression
@mark.text_box
@title('check fill fields and submit')
def test_form(driver, session):
    text_box = TextBox(driver, url='text-box')
    text_box.open()
    text_box.fill_text_fields_and_submit(driver, session)
    text_box.check_form(driver, session)
