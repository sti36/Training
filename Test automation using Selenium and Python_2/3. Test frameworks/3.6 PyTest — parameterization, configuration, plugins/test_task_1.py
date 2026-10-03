"""Задание: авторизация на сайте
Для следующей задачи вам необходимо авторизоваться на stepik со своим логином и паролем. Пожалуйста, будьте внимательны и не добавляйте свои логин и пароль в публичные репозитории на GitHub. 

Ваша задача -- реализовать автотест со следующим набором действий:

открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
авторизоваться со своими логином и паролем 
дождаться того, что поп-апа с авторизацией больше нет
После того как авторизация успешно пройдет, переходите к следующему шагу. """

# Логин и пароль для авторизации храняться локально в файле config.json

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pathlib import Path

url = 'https://stepik.org/lesson/236895/step/1'

@pytest.fixture(scope="session")
def load_config():
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"
    with open(config_path, "r", encoding="utf-8") as config_file:
        return json.load(config_file)

class Test_Authorization:
    def test_authorization_stepik(self, browser, load_config):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        
        browser.get(url)
        wite = WebDriverWait(browser, 10)

        wite.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth.navbar__auth_login"))).click()
        wite.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))).send_keys(login)
        browser.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        browser.find_element(By.XPATH, "//button[text()='Войти']").click()
        wite.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='User avatar']")))