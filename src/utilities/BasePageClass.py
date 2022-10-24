from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageClass:
    
    _URL = None

    def go(self):
        self.driver.get(self._URL)

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((locator[0], locator[1])))