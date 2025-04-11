"""Интересное число 🤔
Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет, интересное число или нет. Если число интересное, следует вывести текст «Число интересное» (без кавычек), иначе – «Число неинтересное» (без кавычек).

Формат входных данных
На вход программе подается целое трёхзначное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

number = int(input())

third_number = number % 10
second_number = (number % 100) // 10
first_number = (number % 1000) // 100

difference = (first_number + second_number + third_number) - (max(first_number, second_number, third_number) + min(first_number, second_number, third_number))
if (max(first_number, second_number, third_number) - min(first_number, second_number, third_number)) == difference:
    print('Число интересное')
else:
    print('Число неинтересное')