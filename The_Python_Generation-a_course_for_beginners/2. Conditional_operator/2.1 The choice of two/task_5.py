"""Арифметическая прогрессия
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии."""

first_member_progression, second_member_progression, third_member_progression = int(input()), int(input()), int(input())

if (second_member_progression - first_member_progression) + second_member_progression == third_member_progression:
    print('YES')
else:
    print('NO')