"""Звёздная рамка 🌟
На вход программе подаётся натуральное число n(n∈[3;19]). Напишите программу, которая печатает звёздную рамку размерами n×19.

Формат входных данных
На вход программе подаётся натуральное число n(n∈[3;19]) – высота звёздной рамки.

Формат выходных данных
Программа должна вывести звёздную рамку размерами n×19.

Подсказка. Для печати звёздной линии используйте умножение строки на число."""

n = int(input())

for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19)
    else:
        print('*', ' ' * 15, '*')