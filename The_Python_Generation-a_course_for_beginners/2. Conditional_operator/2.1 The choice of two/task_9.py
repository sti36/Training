"""Только + 🌶️
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел."""

NULL = 0

first_number, second_number, third_number = int(input()), int(input()), int(input())

if first_number < NULL:
    first_number = 0

if second_number < NULL:
    second_number = 0

if third_number < NULL:
    third_number = 0

print(first_number + second_number + third_number)