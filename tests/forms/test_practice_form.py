from pytest import mark

from pages.practice_form_page import FormPage


@mark.C0003
@mark.regression
@mark.text_box
def test_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    person = form_page.fill_fields_and_submit(driver)
    result = form_page.form_result(driver)
    print(person)
    print(result)
    assert f'{person.first_name} {person.last_name}' == result[0], 'the form has not been failed'
    assert person.email == result[1], 'the form has not been failed'
