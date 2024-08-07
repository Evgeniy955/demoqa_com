from allure import step
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from conftest import driver


class BasePage:

    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url

    @step('open browser')
    def open(self):
        self.driver.get(f'https://demoqa.com/{self.url}')

    @classmethod
    def find_current_element(cls, driver, locator, timeout=10):
        return Wait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def find_current_elements(cls, driver, locator, timeout=10):
        return Wait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @classmethod
    @step('remove footer')
    def remove_footer(cls, driver):
        driver.execute_script("document.getElementsByTagName('footer')[0].remove()")
        driver.execute_script("document.getElementById('fixedban').style.display='none'")

    @classmethod
    @step('check block elements')
    def check_block_elements(cls, driver, dict_names, locator):
        for item_name, item_key in dict_names.items():
            for num in range(len(item_key)):
                item_text = cls.find_current_elements(driver, locator[item_name])[num]
                item_text.is_displayed()
                print(item_text.text, item_key[num])
                assert item_text.text == item_key[num], "Wrong label text"

    @classmethod
    @step('scroll to element')
    def scroll_into_view(cls, driver, locator):
        elem = cls.find_current_element(driver, locator)
        if elem.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)

