from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


# Waits and retries
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def wait_for_presence_of_element(self, by, value, timeouts=10, retries=3):
        for attempt in range(retries):
            try:
                return WebDriverWait(self.driver, timeouts).until(EC.presence_of_element_located((by, value)))

            except StaleElementReferenceException:
                print(f'StaleElementReferenceException occured in {attempt + 1}')

            except TimeoutException:
                print(
                    f'TimeoutException occured in {attempt + 1} no element found by {by} with value {value} after retry {retries}')

    def wait_for_presence_of_elements(self, by, value, timeouts=20):
        return WebDriverWait(self.driver, timeouts).until(EC.presence_of_all_elements_located((by, value)))
