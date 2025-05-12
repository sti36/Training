"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""

first_list_numbers = [int(i) for i in input().split()] 
second_list_number = []

for i in first_list_numbers:
    if first_list_numbers.count(i) > 1 and second_list_number.count(i) == 0:
        second_list_number.append(i)
        
for i in second_list_number:
    print(i, end=" ")