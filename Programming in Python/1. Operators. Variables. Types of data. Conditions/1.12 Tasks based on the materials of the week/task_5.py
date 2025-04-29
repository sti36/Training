"""Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа."""

first_number, second_number, third_number = int(input()), int(input()), int(input())

if first_number >= second_number >= third_number:
    print(first_number, third_number, second_number, sep='\n')

elif first_number >= third_number >= second_number:
    print(first_number, second_number, third_number, sep='\n')

elif second_number >= first_number >= third_number:
    print(second_number, third_number, first_number, sep='\n')

elif second_number >= third_number >= first_number:
    print(second_number, first_number, third_number, sep='\n')

elif third_number >= first_number >= second_number:
    print(third_number, second_number, first_number, sep='\n')
    
elif third_number >= second_number >= first_number:
    print(third_number, first_number, second_number, sep='\n')