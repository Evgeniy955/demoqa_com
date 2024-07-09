from pytest import mark

from pages.practice_form_page import FormPage


@mark.regression
@mark.critical_priority
@mark.practice_form_test
def test_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    person = form_page.fill_fields_and_submit(driver)
    result = form_page.form_result(driver)
    print(person)
    print(result)
    assert f'{person.first_name} {person.last_name}' == result[0], 'the form has not been failed'
    assert person.email == result[1], 'the form has not been failed'


@mark.regression
@mark.medium_priority
@mark.practice_form_test
def test_elements_of_practice_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    form_page.check_field_name_of_practice_form(driver)
    form_page.check_button_and_checkbox_names(driver)


@mark.xfail
@mark.practice_form_test
@mark.high_priority
def test_wrong_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    form_page.fail_test(driver)
