"""Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы."""

initial_multipliable_number, final_multipliable_number, initial_multiplier, final_multiplier = int(input()), int(input()), int(input()), int(input())
#Рисуем шапку таблицы
for k in range (initial_multiplier, final_multiplier + 1):
    print('\t' + str(k), end='')
print(end='\n')
#Считаем и рисуем таблицу
for i in range(initial_multipliable_number, final_multipliable_number + 1):
    print(str(i) + '\t', end='')
    for j in range(initial_multiplier, final_multiplier + 1):
        print(str(i * j), end='\t')
    print(end='\n')