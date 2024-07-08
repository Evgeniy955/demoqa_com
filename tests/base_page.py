from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from conftest import driver


class BasePage:

    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url

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

    @classmethod
    def check_block_elements(cls, driver, dict_names, locator):
        for item_name, item_key in dict_names.items():
            for num in range(len(item_key)):
                item_text = cls.find_current_elements(driver, locator[item_name])[num]
                item_text.is_displayed()
                print(item_text.text, item_key[num])
                assert item_text.text == item_key[num], "Wrong label text"

    @classmethod
    def scroll_into_view(cls, driver, locator):
        elem = cls.find_current_element(driver, locator)
        if elem.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", locator())

    @classmethod
    def scroll(cls, driver):
        w = driver.get_window_size().get("width")
        h = driver.get_window_size().get("height")

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver,
                                            mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(w / 2, h / 2)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(w / 2, h / 2)
        actions.perform()

    @classmethod
    def move_cursor_to_element(cls, driver, locator):
        iframe = cls.find_current_element(driver, locator)
        ActionChains(driver) \
            .scroll_to_element(iframe) \
            .perform()
