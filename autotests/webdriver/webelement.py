from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond


class WebElement(object):
    def __init__(self, webdriver, selector_type: By, selector: str):
        self._webdriver = webdriver
        self._selector_type = selector_type
        self._selector = selector

    def find(self, timeout: int = 0):
        if timeout == 0:
            return self._webdriver.find_element(self._selector_type, self._selector)
        else:
            return WebDriverWait(self._webdriver, timeout).until(
                ExpCond.presence_of_element_located((self._selector_type, self._selector)))

    def wait_clickable(self, timeout: int):
        return WebDriverWait(self._webdriver, timeout).until(
            ExpCond.element_to_be_clickable((self._selector_type, self._selector)))
