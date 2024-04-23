import time
from PageObjects.cart_page.CartPage import CartPage
from PageObjects.checkout_overview_page.CheckoutOverviewPage import CheckoutOverviewPage
from PageObjects.checkout_your_info_page.CheckoutYourInfoPage import CheckoutYourInfoPage
from PageObjects.checkout_complete_page.CheckoutCompletePage import CheckoutCompletePage
from PageObjects.home_page.HomePage import HomePage
from PageObjects.login_page.LoginPage import LoginPage
from TestData.Test_Data import Test_Data

from Utilities.constants import Constants
from Utilities.conftest import *


@pytest.mark.usefixture("driver")
class TestBuyItem:

    def test_login_correct_credentials(self, driver):
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
        driver.implicitly_wait(5)

    def test_go_to_cart(self, driver):
        self.home_page = HomePage(driver)
        driver.implicitly_wait(5)
        self.home_page.click_add_to_cart_cta()
        driver.implicitly_wait(5)
        self.home_page.click_cart_icon()

    def test_checkout(self, driver):
        self.cart_page = CartPage(driver)
        time.sleep(2)
        self.cart_page.click_checkout_cta()
        time.sleep(2)

    def test_enter_details(self, driver):
        self.checkout_your_info_page = CheckoutYourInfoPage(driver)
        self.test_data = Test_Data()
        self.checkout_your_info_page.enter_first_name(self.test_data.first_name)
        time.sleep(2)
        self.checkout_your_info_page.enter_last_name(self.test_data.last_name)
        time.sleep(2)
        self.checkout_your_info_page.enter_zip_code(self.test_data.zip_code)
        time.sleep(2)
        self.checkout_your_info_page.click_continue_cta()
        time.sleep(2)

    def test_finish_checkout(self, driver):
        self.checkout_overview_page = CheckoutOverviewPage(driver)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.checkout_overview_page.click_finish_cta()

    def test_checkout_complete(self, driver):
        time.sleep(2)
        self.checkout_complete_page = CheckoutCompletePage(driver)
        time.sleep(2)
        self.checkout_complete_page.click_back_home_cta()
        time.sleep(2)
