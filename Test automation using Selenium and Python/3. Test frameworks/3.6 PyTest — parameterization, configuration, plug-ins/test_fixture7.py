import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(driver, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")