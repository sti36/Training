"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"""

#Изменение кода: Отключен интерфейс браузера, добавлено копирование ответа из алерта и его вывод в терминал

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

url = 'http://suninjuly.github.io/file_input.html'
first_name = 'Sergey'
last_name = 'Shmakov'
email = 'email@mail.ru'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'task_3.txt'
file_path = os.path.join(current_dir, file_name)

options = Options()
options.add_argument('--headless=new')

try:
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    browser.find_element(By.XPATH, '//input[@name = "firstname"]').send_keys(first_name)
    browser.find_element(By.XPATH, '//input[@name = "lastname"]').send_keys(last_name)
    browser.find_element(By.XPATH, '//input[@name = "email"]').send_keys(email)

    browser.find_element(By.XPATH, '//input[@id = "file"]').send_keys(file_path)

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    number = alert.text.split()[-1]  # извлекает последнее слово (число) из текста алерта
    alert.accept()
    print(f"Answer: {number}")

finally:
    browser.quit()