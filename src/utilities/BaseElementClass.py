from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.Locator import Locator
from utilities.Logger import Logger
import logging
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    InvalidElementStateException,
)


class BaseElement:
    logger = Logger(logging.DEBUG)

    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.is_element_present()
        self.logger.info(f"Element {self.locator} found")

    def insert_text(self, text):
        # self.element.clear()
        self.element.send_keys(text)
        self.logger.info(f"Inserting text '{text}' into element {self.locator}")

    def click_element(self):
        try:
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element)
            self.element.location_once_scrolled_into_view
            self.is_element_clickable().click()
            self.logger.info(f"Clicking element {self.locator}")
            # self.element.click()
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not clickable") from e

    def clear_field(self):
        try:
            self.element.clear()
        except InvalidElementStateException as e:
            self.logger.error(
                f"Element {self.locator} is not currently interactable and may not be manipulated"
            )
            raise InvalidElementStateException(
                f"Element {self.locator} not interactable"
            ) from e

    def get_text(self):
        self.is_element_visible()
        return self.element.text

    def get_all_elements(self) -> List[WebElement]:
        elements = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_all_elements_located(
                (self.locator.method, self.locator.location)
            )
        )
        return elements

    def is_element_visible(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((locator.method, locator.location))
        )

    def is_element_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable((locator.method, locator.location))
        )

    def is_selected(self):
        return self.element.is_selected()

    def is_visible(self):
        try:
            self.is_element_visible()
            self.logger.info(f"Element {self.locator} is visible")
            return True
        except TimeoutException:
            self.logger.error(f"Element {self.locator} is not visible")
            return False

    def is_element_present(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located(
                    (self.locator.method, self.locator.location)
                )
            )
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not found") from e
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element {self.locator} not found") from e

    def is_element_visible(self):
        try:
            self.is_element_present()
            return WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of(self.element)
            )
        except TimeoutException:
            return False

    def is_element_clickable(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.element_to_be_clickable(self.element)
            )
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not clickable") from e
