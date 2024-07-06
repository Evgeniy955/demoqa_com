from pytest import mark

from tests.alerts_frame_windows.pages.alerts_page import Alerts


@mark.C0005
@mark.regression
@mark.alerts_page
def test_alerts_page_elements(driver):
    alerts_page = Alerts(driver, 'alerts')
    alerts_page.open()
    alerts_page.check_elements_on_alerts_page(driver)


@mark.C0006
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
