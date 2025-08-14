"""Задание: авторизация на сайте
Для следующей задачи вам необходимо авторизоваться на stepik со своим логином и паролем. Пожалуйста, будьте внимательны и не добавляйте свои логин и пароль в публичные репозитории на GitHub. 

Ваша задача -- реализовать автотест со следующим набором действий:

открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
авторизоваться со своими логином и паролем 
дождаться того, что поп-апа с авторизацией больше нет
После того как авторизация успешно пройдет, переходите к следующему шагу. 

ВАЖНО!!!
Логин и пароль для авторизации храняться локально в файле config.json"""

import time
import math
import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('C:\\Users\\cool_\\Desktop\\Training\\Test automation using Selenium and Python\\3. Test frameworks\\3.6 PyTest — parameterization, configuration, plug-ins\\authorization\\config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
    
def test_authorization_stepik_answer(driver, link, load_config):
    login = load_config['login_stepik']
    password = load_config['password_stepik']

    driver.get(link)
    wite = WebDriverWait(driver, 10)

    # Авторизация
    wite.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Войти"]'))).click()        
    wite.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="login"]'))).send_keys(login)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Войти"]').click()

    # Получаем правильный ответ
    answer = str(math.log(int(time.time())))
    # Очистка поля
    wite.until(EC.visibility_of_element_located((By.XPATH, '//textarea[(contains@class, "ember-text-area")]'))).clear()
    # Ввод результата
    wite.until(EC.visibility_of_element_located((By.XPATH, '//textarea[(contains@class, "ember-text-area")]'))).send_keys(answer)
    # Ожидание кнопки "Отправить" на кликабельность
    wite.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]')))
    # Отправляем результат
    driver.find_element(By.XPATH, '//button[text()="Отправить"]').click()
    # Дожидаемся появления фидбэка
    feedback_message = wite.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]'))).text()
    
    assert feedback_message != "Correct!", f'Часть ответа: {feedback_message}.'