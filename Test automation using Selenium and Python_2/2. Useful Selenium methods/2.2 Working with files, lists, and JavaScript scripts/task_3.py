"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

url = 'http://suninjuly.github.io/file_input.html'
first_name = 'Sergey'
last_name = 'Shmakov'
email = 'email@mail.ru'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'task_3.txt'
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.XPATH, '//input[@name = "firstname"]').send_keys(first_name)
    browser.find_element(By.XPATH, '//input[@name = "lastname"]').send_keys(last_name)
    browser.find_element(By.XPATH, '//input[@name = "email"]').send_keys(email)

    browser.find_element(By.XPATH, '//input[@id = "file"]').send_keys(file_path)

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

finally:
    time.sleep(3)
    browser.quit()