"""Сортировка чисел
На вход программе подаётся строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

Формат входных данных
На вход программе подаётся строка текста, содержащая целые числа, разделённые символом пробела.

Формат выходных данных
Программа должна вывести две строки текста в соответствии с условием задачи."""

input_string = input()

numbers = list(map(int, input_string.split())) # Преобразование строки в список целых чисел

# Сортируем список по возрастанию и выводим
sorted_ascending = sorted(numbers)
print(*sorted_ascending)

# Сортируем список по убыванию и выводим
sorted_descending = sorted(numbers, reverse=True)
print(*sorted_descending)