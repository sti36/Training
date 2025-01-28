"""Перестановка цифр
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа."""

number = int(input())

last_digit = number % 10
second_digit = (number % 100) // 10
third_digit = number // 100

print(third_digit, second_digit, last_digit, sep='')
print(third_digit, last_digit, second_digit, sep='')
print(second_digit, third_digit, last_digit, sep='')
print(second_digit, last_digit, third_digit, sep='')
print(last_digit, third_digit, second_digit, sep='')
print(last_digit, second_digit, third_digit, sep='')