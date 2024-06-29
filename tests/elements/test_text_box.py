from selenium.webdriver.common.by import By

from tests.elements.pages.text_box_page import TextBox


def test_form(driver, session):
    text_box_page = TextBox(driver, 'text-box')
    text_box_page.open()
    text_box_page.fill_text_fields_and_submit(session)
    text_box_page.check_placeholders()
    text_box_page.check_form(session)
