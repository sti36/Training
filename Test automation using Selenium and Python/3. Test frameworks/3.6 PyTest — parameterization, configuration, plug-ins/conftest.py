import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Firefox()
    yield driver
    print("\nquit browser..")
    driver.quit()