"""Задание: вывод PyTest
Попробуйте запустить ваши тесты из урока 3.2 https://stepik.org/lesson/36285/step/13 с помощью PyTest. В выводе найдите последнюю строку, скопируйте её и отправьте в это задание. Отправьте текст, который находится между  === и ===.

PS Обратите внимание - предупреждений (warnings) в вашем ответе быть не должно."""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_first():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    input_first_name.send_keys('Ivan')

    input_last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    input_last_name.send_keys('Ivanov')

    input_email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    input_email.send_keys('Email')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert("Congratulations! You have successfully registered!", welcome_text, f"Welcome Text не совпадает с {welcome_text}")

    # закрываем браузер после всех манипуляций
    browser.quit()


def test_second():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    input_first_name.send_keys('Ivan')

    input_last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    input_last_name.send_keys('Ivanov')

    input_email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    input_email.send_keys('Email')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert("Congratulations! You have successfully registered!", welcome_text, f"Welcome Text не совпадает с {welcome_text}")

    # закрываем браузер после всех манипуляций
    browser.quit()

if __name__ == "__main__":
    pytest.main()