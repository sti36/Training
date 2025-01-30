"""Принадлежность 2
Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам."""

LOWER_LIMIT_ON = -3
UPPER_LIMIT_ON = 7

number = int(input())

if LOWER_LIMIT_ON < number < UPPER_LIMIT_ON:
    print('Не принадлежит')
else:
    print('Принадлежит')