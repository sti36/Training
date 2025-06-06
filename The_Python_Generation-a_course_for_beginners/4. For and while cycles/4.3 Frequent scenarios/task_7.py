"""Сумма делителей
На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

Входные данные
На вход программе подаётся натуральное число n.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание 1. Сумма делителей числа – это сумма всех чисел, на которые данное число делится без остатка. Например, делители числа 12 – это числа 1,2,3,4,6,12. Их сумма равна 1+2+3+4+6+12=28.

Примечание 2. Функция подсчёта суммы всех делителей числа является очень важной в теории чисел."""

number = int(input())
sum = 0

for i in range(1, number + 1):
    if number % i == 0:
        sum += i
print(sum)