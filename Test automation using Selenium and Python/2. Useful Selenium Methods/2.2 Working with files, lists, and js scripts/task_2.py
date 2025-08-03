"""Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def serch_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу https://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    # Считать значение для переменной x.
    x_element = browser.find_element(By.ID, 'input_value').text

    # Посчитать математическую функцию от x.
    x_answer = serch_x(x_element)

    # Проскроллить страницу вниз.
    button_submit = browser.find_element(By.XPATH, "/html/body/div/form/button")
    browser.execute_script("window.scrollBy(0, 150);")

    # Ввести ответ в текстовое поле.
    input_answer = browser.find_element(By.ID, 'answer').send_keys(x_answer)

    # Выбрать checkbox "I'm the robot".
    browser.find_element(By.ID, 'robotCheckbox').click()

    # Переключить radiobutton "Robots rule!".
    browser.find_element(By.ID, 'robotsRule').click()

    # Нажать на кнопку "Submit".
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()