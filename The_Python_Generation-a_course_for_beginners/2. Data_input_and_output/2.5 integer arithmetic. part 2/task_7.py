"""Напишите программу, которая рассчитывает сумму и произведение цифр положительного трёхзначного числа и выводит текст в следующем формате:

Сумма цифр = <сумма цифр>
Произведение цифр = <произведение цифр>"""

number = int(input())

last_digit = number % 10
second_digit = (number % 100) // 10
third_digit = number // 100

print('Сумма цифр =', last_digit + second_digit + third_digit)
print('Произведение цифр =', last_digit * second_digit * third_digit)