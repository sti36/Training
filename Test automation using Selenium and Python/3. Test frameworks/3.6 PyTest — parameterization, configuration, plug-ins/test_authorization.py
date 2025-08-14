"""Задание: авторизация на сайте
Для следующей задачи вам необходимо авторизоваться на stepik со своим логином и паролем. Пожалуйста, будьте внимательны и не добавляйте свои логин и пароль в публичные репозитории на GitHub. 

Ваша задача -- реализовать автотест со следующим набором действий:

открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
авторизоваться со своими логином и паролем 
дождаться того, что поп-апа с авторизацией больше нет
После того как авторизация успешно пройдет, переходите к следующему шагу.

ВАЖНО!!!
Логин и пароль для авторизации храняться локально в файле config.json"""

import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://stepik.org/lesson/236895/step/1'

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('C:\\Users\\cool_\\Training\\Test automation using Selenium and Python\\3. Test frameworks\\3.6 PyTest — parameterization, configuration, plug-ins\\authorization\\config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

class Test_Authorization:
    def test_authorization_stepik(self, driver, load_config):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        
        driver.get(link)
        wite = WebDriverWait(driver, 10)

        wite.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/lesson/236895/step/1?auth=login']"))).click()
        wite.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))).send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        wite.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='User avatar']")))