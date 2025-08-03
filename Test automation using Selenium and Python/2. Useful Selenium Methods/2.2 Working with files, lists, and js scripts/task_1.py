"""Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже должен пройти успешно."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

first_link = 'http://suninjuly.github.io/selects1.html'
second_link = 'http://suninjuly.github.io/selects2.html'

def dropdown(link):
    sum = 0

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = browser.find_element(By.ID, 'num1').text
        y = browser.find_element(By.ID, 'num2').text
        sum = int(x) + int(y)

        select = Select(browser.find_element(By.ID, 'dropdown'))
        select.select_by_value(str(sum))

        browser.find_element(By.XPATH, '/html/body/div/form/button').click()
    
    finally:
        time.sleep(5)
        browser.quit()

dropdown(first_link)
dropdown(second_link)