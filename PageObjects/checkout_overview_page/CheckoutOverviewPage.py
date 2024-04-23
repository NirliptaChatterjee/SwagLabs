from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class CheckoutOverviewPage(BasePage):
    finish_cta_xpath = (By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']")

    def click_finish_cta(self):
        self.wait_for_presence_of_element(*self.finish_cta_xpath).click()
