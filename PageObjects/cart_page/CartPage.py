from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class CartPage(BasePage):
    item_name_xpath = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    add_to_cart_cta_xpath = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    remove_cta_xpath = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    checkout_cta_xpath = (By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']")

    def click_checkout_cta(self):
        self.wait_for_presence_of_element(*self.checkout_cta_xpath).click()
