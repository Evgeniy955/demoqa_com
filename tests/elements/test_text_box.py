from allure import title
from pytest import mark

from tests.elements.pages.text_box_page import TextBox


@mark.medium_priority
@mark.text_box_test
@title('check text box form elements')
def test_elements_of_text_box_form(driver, session):
    text_box = TextBox(driver, url='text-box')
    text_box.open()
    text_box.elements_on_text_box_page(driver)
    text_box.check_placeholders(driver)


@mark.regression
@mark.critical_priority
@mark.text_box_test
@title('check fill fields and submit')
def test_form(driver, session):
    text_box = TextBox(driver, url='text-box')
    text_box.open()
    text_box.fill_text_fields_and_submit(driver, session)
    text_box.check_form(driver, session)
