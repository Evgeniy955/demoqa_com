from pytest import mark

from tests.alerts_frame_windows.pages.alerts_page import Alerts
from utils.helper_methods import test_number


@test_number("05")
@mark.regression
@mark.alerts_page
def test_alerts_page_elements(driver):
    alerts_page = Alerts(driver, 'alerts')
    alerts_page.open()
    alerts_page.check_elements_on_alerts_page(driver)


@test_number("06")
@mark.regression
@mark.alerts_page
def test_click_on_alert_button(driver):
    alerts_page = Alerts(driver, 'alerts')
    alerts_page.open()
    alerts_page.click_on_alert_button(driver)
    alerts_page.click_timer_alert_button(driver)
    alerts_page.click_confirm_button(driver)
    alerts_page.click_decline_button(driver)
    alerts_page.click_prompt(driver)
