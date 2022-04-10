import logging

from selenium.webdriver.common.by import By

from autotests.webdriver.webelement import WebElement


class EmailSignInPage(object):
    def __init__(self, webdriver, domain):
        # service elements
        self._log = logging.getLogger(self.__class__.__name__)
        self._driver = webdriver

        # page url
        self._page_url = f'https://exchange.{domain}/'

        # page elements
        self._email_input = WebElement(self._driver, By.CSS_SELECTOR, "input[data-test='email_input']")

    def wait_page_opened(self, timeout: int):
        self._log.info(f'wait page opened for {timeout} sec')
        self._email_input.find(timeout)
