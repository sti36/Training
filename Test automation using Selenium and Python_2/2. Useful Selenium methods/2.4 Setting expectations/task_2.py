"""Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import math

options = Options()
options.add_argument('--headless=new')

url = 'http://suninjuly.github.io/explicit_wait2.html'

price = '$100'

wait = WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    wait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id = "price"]'), price))
    button_book = browser.find_element(By.XPATH, '//button[text() = "Book"]')
    button_book.click()

    x_element = wait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@id = "input_value"]')))
    x_element = x_element.text
    answer_math = calc(x_element)
    answer_input = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    answer_input.send_keys(answer_math)
    answer_button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    answer_button.click()

    answer_task = browser.switch_to.alert.text.split()[-1]
    print(f'Answer: {answer_task}')

finally:
    browser.quit()