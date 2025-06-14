"""Сумма чисел
На вход программе подаётся строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

Формат входных данных
На вход программе подаётся строка текста, содержащая натуральные числа, разделённые символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

seq = input().split()
expression = "+".join(seq)

sm = 0
for el in seq:
    sm += int(el)
expression += f"={sm}"

print(expression)