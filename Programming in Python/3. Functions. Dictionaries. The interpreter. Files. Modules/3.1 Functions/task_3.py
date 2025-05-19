"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации."""

#list = [321, 342, 5654, 234123, 75675, 423432, 21312312, 56546, 1]

def modify_list(list):
    i = 0
    while i < len(list):
        if list[i] % 2 != 0:
            del (list[i])
        else:
            list[i] = list[i] // 2 
            i += 1
#modify_list(list)
#print(list)