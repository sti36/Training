"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание."""

#Работа браузер без интерфейсной части

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import math

options = Options()
options.add_argument('--headless=new')

url = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    browser.find_element(By.XPATH, '//button[text() = "I want to go on a magical journey!"]').click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]').text
    answer_math = calc(x_element)
    browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(answer_math)
    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    answer_task = browser.switch_to.alert.text.split()[-1]
    print(f'Answer: {answer_task}')

finally:
    browser.quit()