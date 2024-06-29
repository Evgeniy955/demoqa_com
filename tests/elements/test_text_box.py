from tests.elements.pages.text_box_page import TextBox


def test_form(driver, session):
    text_box = TextBox(driver, url='text-box')
    text_box.open()
    text_box.fill_text_fields_and_submit(driver, session)
    text_box.check_placeholders(driver)
    text_box.check_form(driver, session)
