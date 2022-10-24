from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class Locator:
    location: str
    method: str = By.CSS_SELECTOR