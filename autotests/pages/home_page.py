import logging

from selenium.webdriver.common.by import By

from autotests.webdriver.webelement import WebElement


class HomePage(object):
    def __init__(self, webdriver, domain):
        # service elements
        self._log = logging.getLogger(self.__class__.__name__)
        self._driver = webdriver

        # page url
        self._page_url = f'https://exchange.{domain}/'

        # page elements
        self._from_amount_input = WebElement(self._driver, By.CSS_SELECTOR, "input[data-test='from_amount_input']")
        self._from_currency_btn = WebElement(self._driver, By.CSS_SELECTOR, "button[data-test='from_amount_select']")
        self._from_currency_list = WebElement(self._driver, By.CSS_SELECTOR, "div[data-test='from_currencies_modal']")

        self._to_amount_input = WebElement(self._driver, By.CSS_SELECTOR, "input[data-test='to_amount_input']")

        self._wallet_address_input = WebElement(self._driver, By.CSS_SELECTOR, "textarea[data-test='address_input']")

        self._terms_btn = WebElement(self._driver, By.CSS_SELECTOR, "button[data-test='amount_switch']")

        self._buy_btn = WebElement(self._driver, By.CSS_SELECTOR, "button[data-test='amount_button']")

    def open_page(self, timeout: int):
        self._log.info(f'open page {self._page_url} during {timeout} sec')
        self._driver.get(self._page_url)
        self.wait_page_opened(timeout)

    def wait_page_opened(self, timeout: int):
        self._log.info(f'wait page opened for {timeout} sec')
        self._from_amount_input.find(timeout)

    def set_from_amount(self, value):
        self._log.info(f'set From Amount value to {value}')
        self._from_amount_input.find().clear()
        self._from_amount_input.find().send_keys(value)

    def set_to_amount(self, value):
        self._log.info(f'set To Amount value to {value}')
        self._to_amount_input.find().clear()
        self._to_amount_input.find().send_keys(value)

    def set_wallet_address(self, value):
        self._log.info(f'set Wallet Address value to {value}')
        self._wallet_address_input.find().clear()
        self._wallet_address_input.find().send_keys(value)

    def click_terms_btn(self):
        self._log.info(f'click Terms button')
        self._terms_btn.find().click()

    def click_buy_btn(self, timeout: int):
        self._log.info(f'click Buy button during {timeout} sec')
        self._buy_btn.wait_clickable(timeout).click()
