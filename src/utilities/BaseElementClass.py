from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locator import Locator


class BaseElement:
    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.element_is_visible(self.locator)

    def insert_text(self, text):
        self.element.send_keys(text)

    def click_field(self):
        self.element_is_clickable(self.locator)
        self.element.click()

    def clear_field(self):
        self.element.clear()

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((locator.method, locator.location))
        )

    def element_is_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable((locator.method, locator.location))
        )
