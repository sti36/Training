"""Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def scroll(element):
   return browser.execute_script("return arguments[0].scrollIntoView(true);", element)

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.XPATH, '//span[@id = "input_value"]').text
    answer = calc(x)

    browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(answer)

    checkbox = browser.find_element(By.XPATH, '//input[@id = "robotCheckbox"]')
    checkbox.click()

    radio_button = browser.find_element(By.XPATH, '//input[@id = "robotsRule"]')
    scroll(radio_button)
    radio_button.click()

    button_submit = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    scroll(button_submit)
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()