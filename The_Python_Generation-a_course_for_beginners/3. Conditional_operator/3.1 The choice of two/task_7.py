"""Наименьшее из четырёх чисел 🌶️
Напишите программу, которая определяет наименьшее из четырёх чисел."""

first_number, second_number, third_number, fourth_number = int(input()), int(input()), int(input()), int(input())

if first_number > second_number:
    first_minimum = second_number
else:
    first_minimum = first_number

if third_number > fourth_number:
    second_minimum = fourth_number
else:
    second_minimum = third_number

if first_minimum > second_minimum:
    print(second_minimum)
else:
    print(first_minimum)