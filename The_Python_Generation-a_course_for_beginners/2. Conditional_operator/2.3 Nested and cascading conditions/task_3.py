"""Серединное число
Даны три различных целых числа. Напишите программу, которая находит серединное значение из этих чисел."""

first_number, second_numer, third_number = int(input()), int(input()), int(input())

if first_number < second_numer < third_number or third_number < second_numer < first_number:
    print(second_numer)
elif second_numer < first_number < third_number or third_number < first_number < second_numer:
    print(first_number)
else:
    print(third_number)