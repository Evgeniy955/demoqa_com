import allure
from allure import title
from pytest import mark

from pages.practice_form_page import FormPage


@mark.C0006
@mark.regression
@mark.critical_priority
@mark.practice_form_test
@allure.story("test form")
@allure.feature("practice form test")
@title('test practice form')
def test_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    person = form_page.fill_fields_and_submit(driver)
    result = form_page.form_result(driver)
    print(person)
    print(result)
    assert f'{person.first_name} {person.last_name}' == result[0], 'the form has not been failed'
    assert person.email == result[1], 'the form has not been failed'


@mark.C0007
@mark.regression
@mark.medium_priority
@mark.practice_form_test
@allure.story("test elements of practice form")
@allure.feature("practice form test")
@title('test elements of practice form')
def test_elements_of_practice_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    form_page.check_field_name_of_practice_form(driver)
    form_page.check_button_and_checkbox_names(driver)


@mark.C0008
# @mark.xfail
@allure.story("test wrong form")
@allure.feature("practice form test")
@mark.high_priority
@mark.practice_form_test
@title('test wrong form')
def test_wrong_form(driver):
    form_page = FormPage(driver, 'automation-practice-form')
    form_page.open()
    form_page.fail_test(driver)
