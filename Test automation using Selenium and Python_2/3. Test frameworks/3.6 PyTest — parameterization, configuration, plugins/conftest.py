import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options() # Закомментировать строку если нужно отображение интерфейса браузера
    options.add_argument('--headless=new') # Закомментировать строку если нужно отображение интерфейса браузера
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options) # Закомментировать options=options если нужно отображение интерфейса браузера
    yield browser
    print("\nquit browser..")
    browser.quit()