from autotests.pages.email_sign_in_page import EmailSignInPage
from autotests.pages.home_page import HomePage


class PageProvider(object):
    def __init__(self, webdriver, domain):
        self.home_page = HomePage(webdriver, domain)
        self.email_sign_in_page = EmailSignInPage(webdriver, domain)
