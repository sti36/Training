"""Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = 'http://suninjuly.github.io/get_attribute.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.XPATH, '//img[@id = "treasure"]').get_attribute("valuex")
    answer = calc(x)

    browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(answer)

    browser.find_element(By.XPATH, '//input[@id = "robotCheckbox"]').click()

    browser.find_element(By.XPATH, '//input[@id = "robotsRule"]').click()

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

finally:
    time.sleep(30)
    browser.quit()