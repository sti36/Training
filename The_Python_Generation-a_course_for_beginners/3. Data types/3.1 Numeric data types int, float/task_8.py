"""Наибольшее и наименьшее
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел и выводит текст в следующем формате:

Наименьшее число = <наименьшее число>
Наибольшее число = <наибольшее число>
Формат входных данных
На вход программе подаются 5 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

first_number, second_number, third_number, fourth_number, fifth_number = int(input()), int(input()), int(input()), int(input()), int(input())

print('Наименьшее число =', min(first_number, second_number, third_number, fourth_number, fifth_number))
print('Наибольшее число =', max(first_number, second_number, third_number, fourth_number, fifth_number))