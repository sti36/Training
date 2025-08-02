"""Задание: уникальность селекторов
Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся. Также и вам предстоит проверить чужой код. Ознакомившись с разными способами решения одной и той же задачи, вы сможете лучше понять изучаемую тему.

У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте. Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная страница доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.

Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте. 

Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае попробуйте поменять селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии страницы."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    input_first_name.send_keys('Ivan')

    input_last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    input_last_name.send_keys('Ivanov')

    input_email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    input_email.send_keys('Email')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()