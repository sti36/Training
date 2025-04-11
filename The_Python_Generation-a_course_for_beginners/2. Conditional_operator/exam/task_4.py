"""Римские цифры
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона [1;10], то программа должна вывести текст «ошибка» (без кавычек).
Формат входных данных
На вход программе подаётся целое число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

arabic_number = int(input())

if not (1 <= arabic_number <= 10):
    print('ошибка')
elif arabic_number == 1:
    print("I")
elif arabic_number == 2:
    print("II")
elif arabic_number == 3:
    print("III")
elif arabic_number == 4:
    print("IV")
elif arabic_number == 5:
    print("V")
elif arabic_number == 6:
    print("VI")
elif arabic_number == 7:
    print("VII")
elif arabic_number == 8:
    print("VIII")
elif arabic_number == 9:
    print("IX")
elif arabic_number == 10:
    print("X")