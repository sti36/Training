"""Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. """

list_numbers = [int(i) for i in input().split()]
sum = 0

for i in list_numbers[0:]:
    sum += i

print(sum)