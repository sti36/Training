"""Вторая цифра
Дано натуральное число number(number>9). Напишите программу, которая определяет его вторую (с начала) цифру.

Формат входных данных
На вход программе подаётся одно натуральное число, состоящее как минимум из двух цифр.

Формат выходных данных
Программа должна вывести его вторую (с начала) цифру."""

number = int(input())

while number > 9:
    last_digit = number % 10
    number //= 10

print(last_digit)