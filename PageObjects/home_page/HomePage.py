from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class HomePage(BasePage):
    item_name_xpath = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    add_to_cart_cta_xpath = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    remove_cta_xpath = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    cart_icon_xpath = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def click_add_to_cart_cta(self):
        self.wait_for_presence_of_element(*self.add_to_cart_cta_xpath).click()

    def click_cart_icon(self):
        self.wait_for_presence_of_element(*self.cart_icon_xpath).click()
