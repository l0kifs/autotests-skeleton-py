import logging

from autotests.pages.page_provider import PageProvider


class ExchangeUsecases(object):
    def __init__(self, page_provider: PageProvider):
        # service elements
        self._log = logging.getLogger(self.__class__.__name__)
        self._page_provider = page_provider

    def submit_buy_amount(self, amount, wallet_address):
        self._log.info(f'submit buy amount {amount} for wallet {wallet_address}')
        home_page = self._page_provider.home_page
        home_page.open_page(10)
        home_page.set_from_amount(amount)
        home_page.set_wallet_address(wallet_address)
        home_page.click_terms_btn()
        home_page.click_buy_btn(5)
