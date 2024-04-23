from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class LoginPage(BasePage):
    user_name_xpath = (By.XPATH, "//input[@id='user-name']")
    password_xpath = (By.XPATH, "//input[@id='password']")
    login_cta_xpath = (By.XPATH, "//input[@id ='login-button']")

    def enter_user_name(self, username):
        self.wait_for_presence_of_element(*self.user_name_xpath).send_keys(username)

    def enter_password(self, password):
        self.wait_for_presence_of_element(*self.password_xpath).send_keys(password)

    def click_login_cta(self):
        self.wait_for_presence_of_element(*self.login_cta_xpath).click()
