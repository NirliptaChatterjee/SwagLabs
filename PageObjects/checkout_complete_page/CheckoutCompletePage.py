from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class CheckoutCompletePage(BasePage):
    back_home_cta_xpath = (By.XPATH, "//button[@class='btn btn_primary btn_small']")

    def click_back_home_cta(self):
        self.wait_for_presence_of_element(*self.back_home_cta_xpath).click()
