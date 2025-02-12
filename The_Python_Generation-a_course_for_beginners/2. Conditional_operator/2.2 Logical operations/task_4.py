"""Красивое число 🌸🌶️
Назовём число красивым, если оно является четырёхзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае."""

LOWER_LIMIT = 10000
UPPER_LIMIT = 999
FIRST_DIVISOR = 7
SECOND_DIVISOR = 17

number = int(input())

if (UPPER_LIMIT < number < LOWER_LIMIT) and (number % FIRST_DIVISOR == 0 or number % SECOND_DIVISOR == 0):
    print('YES')
else:
    print('NO')