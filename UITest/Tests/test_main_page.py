import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("driver_init")
class TestMainPage:

    def initialize(self, driver: WebDriver):
        self.driver: WebDriver = driver