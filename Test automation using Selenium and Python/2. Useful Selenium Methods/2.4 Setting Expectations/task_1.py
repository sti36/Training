"""Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
right_price = '$100'

def search_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    price_on_page = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), right_price))

    driver.find_element(By.XPATH, "//button[@id='book']").click()

    x_element = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    driver.find_element(By.XPATH, "//input[@id='answer']").send_keys(search_x(x_element))
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
finally:
    time.sleep(5)
    driver.quit()