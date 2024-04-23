from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class CheckoutYourInfoPage(BasePage):
    first_name_xpath = (By.XPATH, "//input[@id='first-name']")
    last_name_xpath = (By.XPATH, "//input[@id='last-name']")
    zip_code_xpath = (By.XPATH, "//input[@id='postal-code']")
    continue_cta = (By.XPATH, "//input[@class='submit-button btn btn_primary cart_button btn_action']")

    def enter_first_name(self, firstname):
        self.wait_for_presence_of_element(*self.first_name_xpath).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.wait_for_presence_of_element(*self.last_name_xpath).send_keys(lastname)

    def enter_zip_code(self, zip_code):
        self.wait_for_presence_of_element(*self.zip_code_xpath).send_keys(zip_code)

    def click_continue_cta(self):
        self.wait_for_presence_of_element(*self.continue_cta).click()
