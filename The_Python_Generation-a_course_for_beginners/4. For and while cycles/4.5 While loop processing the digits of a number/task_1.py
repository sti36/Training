"""Обратный порядок 1
Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести цифры введённого числа в столбик в обратном порядке."""

number = int(input())

while number != 0:
    last_digit = number % 10
    print(last_digit)
    number //= 10