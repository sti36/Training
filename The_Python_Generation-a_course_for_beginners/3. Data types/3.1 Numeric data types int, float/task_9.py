"""Сортировка трёх 🔀🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Примечание. Учитывайте, что числа могут быть равны."""

first_number, second_number, third_number = int(input()), int(input()), int(input())

sort = (first_number + second_number + third_number) - (max(first_number, second_number, third_number) + min(first_number, second_number, third_number))
print(max(first_number, second_number, third_number), sort, min(first_number, second_number, third_number), sep='\n')