"""Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b], которые кратны числу 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]. Всего чисел, делящихся на 3, на этом отрезке 6:−3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3."""

first_number, second_number = int(input()), int(input())
sum = 0
count = 0
multiplicity = 3

for i in range(first_number, second_number + 1):
    if i % multiplicity == 0:
        sum += i
        count += 1

print(sum / count)