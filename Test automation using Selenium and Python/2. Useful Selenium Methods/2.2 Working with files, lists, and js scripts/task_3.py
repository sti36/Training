"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('Email')

    # Получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'task_3.txt')
    # Отправляем файл
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.XPATH, '/html/body/div/form/button').click()

finally:
    time.sleep(10)
    browser.quit()