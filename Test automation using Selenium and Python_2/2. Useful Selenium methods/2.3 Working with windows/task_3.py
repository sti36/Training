"""Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import math

options = Options()
options.add_argument('--headless=new')

url = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    browser.find_element(By.XPATH, '//button[text() = "I want to go on a magical journey!"]').click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]').text
    answer_math = calc(x_element)

    browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(answer_math)

    browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    answer_task = browser.switch_to.alert.text.split()[-1]
    print(f'Answer: {answer_task}')

finally:
    browser.quit()