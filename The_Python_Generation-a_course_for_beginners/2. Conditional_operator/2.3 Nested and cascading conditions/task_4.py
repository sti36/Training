"""Количество дней 📅
Дан порядковый номер месяца (1,2,…,12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным."""

month_number = int(input())

if month_number == 2:
    print(28)
elif (month_number < 8 and month_number % 2 == 0) or (month_number > 7 and month_number % 2 != 0):
    print(30)
else:
    print(31)