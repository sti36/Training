"""Задание: вывод PyTest 
Попробуйте запустить ваши тесты из урока 3.2 https://stepik.org/lesson/36285/step/13 с помощью PyTest. В выводе найдите последнюю строку, скопируйте её и отправьте в это задание. Отправьте текст, который находится между  === и ===. 

PS Обратите внимание - предупреждений (warnings) в вашем ответе быть не должно."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest
import time

options = Options()
options.add_argument('--headless=new')

class test_task_5_section_1_6(unittest.TestCase):
    def test_registration_1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome(options=options)
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//label[normalize-space()='First name*']/following-sibling::input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//label[normalize-space()='Last name*']/following-sibling::input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//label[normalize-space()='Email*']/following-sibling::input")
            input3.send_keys("petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не удалась!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome(options=options)
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//label[normalize-space()='First name*']/following-sibling::input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//label[normalize-space()='Last name*']/following-sibling::input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//label[normalize-space()='Email*']/following-sibling::input")
            input3.send_keys("petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не удалась!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()