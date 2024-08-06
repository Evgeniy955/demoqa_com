import allure
from allure import title
from pytest import mark

from tests.alerts_frame_windows.pages.alerts_page import Alerts


@mark.C0001
@mark.regression
@mark.medium_priority
@mark.alerts_page_test
@allure.story("check alerts page elements")
@allure.feature("alerts page test")
@title('check alerts page elements')
def test_alerts_page_elements(driver):
    alerts_page = Alerts(driver, 'alerts')
    alerts_page.open()
    alerts_page.check_elements_on_alerts_page(driver)


@mark.C0002
@mark.regression
@mark.critical_priority
@mark.alerts_page_test
@allure.story("check alert buttons")
@allure.feature("alerts page test")
@title('check alert buttons')
def test_click_on_alert_buttons(driver):
    alerts_page = Alerts(driver, 'alerts')
    alerts_page.open()
    alerts_page.click_on_alert_button(driver)
    alerts_page.click_timer_alert_button(driver)
    alerts_page.click_confirm_button(driver)
    alerts_page.click_decline_button(driver)
    alerts_page.click_prompt(driver)
