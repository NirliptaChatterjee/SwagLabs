import pytest
from selenium import webdriver


# To initialize chrome driver
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
