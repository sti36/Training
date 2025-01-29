"""Наименьшее из двух чисел
Напишите программу, которая определяет наименьшее из двух чисел."""

first_number, second_number = int(input()), int(input())

if first_number < second_number:
    print(first_number)
else:
    print(second_number)