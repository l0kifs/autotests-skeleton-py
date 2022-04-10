import pytest as pytest

from autotests.pages.page_provider import PageProvider
from autotests.usecases.exchange_usecases import ExchangeUsecases
from autotests.webdriver.webdriver import WebDriver, DriverType


@pytest.fixture
def browser():
    webdriver = WebDriver(DriverType.CHROME).get()
    return webdriver


def test_open_email_sign_in_page(browser):
    page_provider = PageProvider(browser, 'mrcr.io')
    exchange_usecases = ExchangeUsecases(page_provider)

    exchange_usecases.submit_buy_amount('100', 'tb1qa4fr4m2ha3hczrf4zrvu22y0gv535qzcphqn6j')
    page_provider.email_sign_in_page.wait_page_opened(10)