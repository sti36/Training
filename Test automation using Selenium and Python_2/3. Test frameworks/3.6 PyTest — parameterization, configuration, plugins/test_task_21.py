'''Задание: параметризация тестов
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

открыть страницу 
авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
ввести правильный ответ (поле перед вводом должно быть пустым)
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"'''

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
from pathlib import Path
import time
import math


@pytest.fixture(scope="session")
def load_config():
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"
    with open(config_path, "r", encoding="utf-8") as config_file:
        return json.load(config_file)


@pytest.mark.parametrize('urls', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_search_message_stepik(browser, load_config, urls):

    answer_math = str(math.log(int(time.time())))

    correct = "Correct!"

    # Получаем логин и пароль из файла config.json
    login = load_config['login_stepik']
    password = load_config['password_stepik']
    wait = WebDriverWait(browser, 30)

    browser.delete_all_cookies()
    browser.refresh()
    time.sleep(5)
    # Запускаем браузер
    browser.get(urls)
    
    # Проходим авторизацию
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "a.navbar__auth.navbar__auth_login"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@name='login']"))).send_keys(login)
    browser.find_element(
        By.XPATH, "//input[@name='password']").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Войти']").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@alt='User avatar']")))

    answer_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//textarea[@placeholder = "Напишите ваш ответ здесь..."]')))
    answer_field.clear()
    answer_field.send_keys(answer_math)

    time.sleep(3)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text() = "Отправить на проверку"]'))).click()

    message = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'smart-hints__hint'))).text

    assert message == correct, "Кусочек сообщения найден!"