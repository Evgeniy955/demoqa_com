import requests
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:

    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url

    # def open(self):
    #     self.driver.get(self.test_url)
    def open(self):
        self.driver.get(f'https://demoqa.com/{self.url}')

    @classmethod
    def find_current_element(cls, driver, locator, timeout=10):
        return Wait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def find_current_elements(cls, driver, locator, timeout=10):
        return Wait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @classmethod
    def remove_footer(cls, driver):
        driver.execute_script("document.getElementsByTagName('footer')[0].remove()")
        driver.execute_script("document.getElementById('fixedban').style.display='none'")
