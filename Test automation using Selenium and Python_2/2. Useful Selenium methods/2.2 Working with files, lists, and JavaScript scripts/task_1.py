"""Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    num_1 = browser.find_element(By.XPATH, '//span[@id = "num1"]').text
    num_2 = browser.find_element(By.XPATH, '//span[@id = "num2"]').text
    answer = int(num_1) + int(num_2)

    Select(browser.find_element(By.XPATH, '//select[@id = "dropdown"]')).select_by_value(str(answer))

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

finally:
    time.sleep(30)
    browser.quit()