from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverType(Enum):
    CHROME = 1
    FIREFOX = 2


class WebDriver(object):
    def __init__(self, driver_type: DriverType):
        self._driver_type = driver_type
        self.headless: bool = False
        webdriver.Chrome().find_element()

    def get(self):
        match self._driver_type:
            case DriverType.CHROME:
                return self._get_chrome()
            case DriverType.FIREFOX:
                return self._get_firefox()

    def _get_chrome(self):
        options = ChromeOptions()
        options.headless = self.headless
        return webdriver.Chrome(options=options)

    def _get_firefox(self):
        options = FirefoxOptions()
        options.headless = self.headless
        return webdriver.Chrome(options=options)

