"""Наибольшие числа 🌶️🌶️
На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел последовательности, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

Формат входных данных
На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два наибольших числа последовательности, каждое на отдельной строке."""

number_iterations_loop = int(input())
first_max_number = 0
second_max_number = 1

for _ in range(number_iterations_loop):
    number = int(input())
    if number > first_max_number:
        second_max_number = first_max_number
        first_max_number = number
    elif number > second_max_number:
        second_max_number = number

print(first_max_number, second_max_number, sep='\n')