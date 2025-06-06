"""Сколько раз?
На вход программе подаётся одна строка. Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *, и выводит текст в следующем формате:

Символ + встречается <n> раз
Символ * встречается <m> раз
где <n>, <m> – количество вхождений символов + и * в строку соответственно.

Формат входных данных
На вход программе подаётся одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

line = str(input())
total_one = 0
total_two = 0

for s in range(0, len(line)):
    if line[s] == '+':
        total_one += 1
    if line[s] == '*':
        total_two += 1

print('Символ + встречается', total_one, 'раз')
print('Символ * встречается', total_two, 'раз')