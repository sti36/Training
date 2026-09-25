"""Задание: поиск элемента по тексту в ссылке
Задание
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

Добавьте в самый верх своего кода import math
Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
str(math.ceil(math.pow(math.pi, math.e)*10000))

                  
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) 

Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

Заполните скриптом форму так же как вы делали в предыдущем шаге урока

После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
Важно! Поиск по тексту ссылки бывает очень удобным, так как часто тексты меняются реже, чем атрибуты элементов. Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут проходить только с определенным языком интерфейса. Применяйте этот метод с осторожностью и помните про возможные ограничения. """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math 

options = Options()
#options.add_argument("--headless=new") #Закомментировать если нужен интерфейс браузера
link = "http://suninjuly.github.io/find_link_text"
text_link_search = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    link_search = browser.find_element(By.XPATH, f'//a[text() = "{text_link_search}"]')
    link_search.click()

    input1 = browser.find_element(By.XPATH, '//input[@name = "first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name = "last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@name = "firstname"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла