import pytest

from Utilities.BasePage import BasePage
from PageObjects.login_page.LoginPage import LoginPage
from TestData.Test_Data import Test_Data
from Utilities.constants import Constants
from Utilities.conftest import driver
from Utilities import constants


@pytest.mark.usefixture("driver")
class TestHomePage:

    def test_login(self, driver):
        self.login_page = LoginPage(driver)
        self.test_data = Test_Data()
        self.constants = Constants()
        driver.get(self.constants.url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        self.login_page.enter_user_name(self.test_data.correct_username)
        driver.implicitly_wait(5)
        self.login_page.enter_password(self.test_data.correct_password)
        driver.implicitly_wait(5)
        self.login_page.click_login_cta()
        driver.implicitly_wait(10)

    # def test_accept_window_alert(self, driver):
    #     driver.switch_to.alert.accept()
    #     driver.implicitly_wait(15)




