"""451 градус по Фаренгейту 🌡️
У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

Для получения градусов по Цельсию из градусов по Фаренгейту используйте следующую формулу:

tC = 5/9(tF − 32)
где tF – температура в градусах по Фаренгейту.

Формат входных данных
На вход программе подаётся одно действительное число – температура в градусах по шкале Фаренгейта.

Формат выходных данных
Программа должна вывести одно действительное число – температуру в градусах по шкале Цельсия."""

temperature_on_Fahrenheit_scale = float(input())

temperature_on_Celsius_scale = 5 / 9 * (temperature_on_Fahrenheit_scale - 32)
print(temperature_on_Celsius_scale)