"""Асимптотическое приближение 📉
На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет значение выражения
(1+(1/2)+(1/3)+...+(1/n)-ln(n)

Формат входных данных
На вход программе подаётся натуральное число n.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math."""

from math import log

number = int(input())
sum = 0

for i in range(1, number):
    sum += 1 / (i + 1)

print(1 + sum - log(number))