"""Без дубликатов
На вход программе подаются натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов."""

repeat_input = int(input())
mas = []

for _ in range(repeat_input):
    line = input()
    if line not in mas:
        mas.append(line)

print(*mas, sep='\n')