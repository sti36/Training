"""Диаграмма
На вход программе подаётся строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.

Формат входных данных
На вход программе подаётся строка текста, содержащая натуральные числа, разделённые символом пробела.

Формат выходных данных
Программа должна вывести столбчатую диаграмму."""

line_numbers = input().split()
plus = '+'

for s in line_numbers:
    print(int(s) * plus)