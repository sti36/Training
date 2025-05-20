"""Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке, каждое на отдельной строке."""

number = int(input())
sum = 0 # Сумма цифр числа
number_digits = 0 # Количество цифр в числе
product_numbers = 1 # Произведение цифр
arithmetic_mean_digits = 0 # Среднее арифметическое цифр
first_number = number % 10 # Первая цифра числа

while number != 0:
    digit = number % 10
    sum += digit
    number_digits += 1
    product_numbers *= digit
    arithmetic_mean_digits = sum / number_digits
    number = number // 10

print(sum, number_digits, product_numbers, arithmetic_mean_digits, digit, digit + first_number, sep='\n')