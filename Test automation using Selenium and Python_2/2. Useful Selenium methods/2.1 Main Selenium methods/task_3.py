"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.

Ваша программа должна выполнить следующие шаги:

Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.XPATH, '//span[@id = "input_value"]').text
    res_x = calc(x)

    browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(res_x)

    browser.find_element(By.XPATH, '//input[@id = "robotCheckbox"]').click()

    browser.find_element(By.XPATH, '//input[@id = "robotsRule"]').click()

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()
finally:
    time.sleep(30)
    browser.quit()