from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.Locator import Locator


class BaseElement:
    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.is_element_visible(self.locator)

    def __getattr__(self, item):
        if hasattr(self.element, item):
            return getattr(self.element, item)

    def insert_text(self, text):
        self.element.send_keys(text)

    def click_field(self):
        self.is_element_clickable(self.locator)
        self.element.click()

    def clear_field(self):
        self.element.clear()

    def is_element_visible(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((locator.method, locator.location))
        )

    def is_element_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable((locator.method, locator.location))
        )
