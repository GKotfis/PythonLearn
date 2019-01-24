import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import urls

@pytest.mark.usefixtures("driver_init")
class TestLoginPage:

    def initialize(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def test_should_have_correct_title(self):
        self.driver.get(urls.LOGIN_PAGE)
        assert "SimData Manager 6.0" in self.driver.title

    def test_should_contain_login_form(self):
        self.driver.get(urls.LOGIN_PAGE)
        self.driver.find_element_by_name("tbxUser")
        self.driver.find_element_by_name("tbxPwd")
        self.driver.find_element_by_name("btnLogin")

    def test_for_incorrect_user_or_password_should_display_error_message(self):
        self.driver.get(urls.LOGIN_PAGE)
        self.driver.find_element_by_name("tbxUser").send_keys("nonexistinguser")
        self.driver.find_element_by_name("tbxPwd").send_keys("somewrongpassword")
        self.driver.find_element_by_name("btnLogin").click()
        self.driver.find_element_by_id("lblError")

    def test_after_positive_authentication_shouldbe_redirect(self):
        self.driver.get(urls.LOGIN_PAGE)
        self.driver.find_element_by_name("tbxUser").send_keys("Administrator")
        self.driver.find_element_by_name("tbxPwd").send_keys("123456789")
        self.driver.find_element_by_name("btnLogin").click()
        assert urls.LOGIN_PAGE not in self.driver.current_url