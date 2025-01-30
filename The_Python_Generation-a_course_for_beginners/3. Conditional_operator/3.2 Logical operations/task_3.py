"""Принадлежность 3
Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам."""

LOWER_BOUNDARY_FIRST_GAP_OFF = -30
UPPER_BOUNDARY_FIRST_GAP_ON = -2
LOWER_BOUNDARY_SECOND_GAP_OFF = 7
UPPER_BOUNDARY_SECOND_GAP_ON = 25

number = int(input())

if LOWER_BOUNDARY_FIRST_GAP_OFF < number <= UPPER_BOUNDARY_FIRST_GAP_ON or LOWER_BOUNDARY_SECOND_GAP_OFF < number <= UPPER_BOUNDARY_SECOND_GAP_ON:
    print('Принадлежит')
else:
    print('Не принадлежит')