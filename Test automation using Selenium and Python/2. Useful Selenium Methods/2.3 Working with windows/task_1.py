"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def search_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//button').click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(search_x(x_element))
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
finally:
    time.sleep(10)
    browser.quit()