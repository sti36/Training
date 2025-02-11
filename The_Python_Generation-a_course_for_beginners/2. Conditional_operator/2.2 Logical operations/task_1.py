"""Принадлежность 1
Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку. """

LOWER_LIMIT = -1
UPPER_LIMIT = 17

number = int(input())

if LOWER_LIMIT < number < UPPER_LIMIT:
    print('Принадлежит')
else:
    print('Не принадлежит')