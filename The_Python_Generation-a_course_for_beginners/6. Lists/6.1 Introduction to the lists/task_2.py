"""Список букв
На вход программе подаётся натуральное число n. Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

Формат входных данных
На вход программе подаётся натуральное число n(1≤n≤26).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

letter_list = []
number = int(input())

for i in range(number):
    letter_list += chr(ord("a") + i)

print(letter_list)