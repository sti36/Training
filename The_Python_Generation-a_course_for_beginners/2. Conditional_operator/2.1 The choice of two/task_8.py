"""Возрастная группа 👧
Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

до 13 (включительно) – детство;
от 14 до 24 (включительно) – молодость;
от 25 до 59 (включительно) – зрелость;
от 60 (включительно) – старость."""

CHILDHOOD = 13
YOUTH_MIN = 14
YOUTH_MAX = 24
MATURE_MIN = 25
MATURE_MAX = 59
OLD = 60

user_age = int(input())

if user_age <= CHILDHOOD:
    print('детство')

if YOUTH_MIN <= user_age <= YOUTH_MAX:
    print('молодость')

if MATURE_MIN <= user_age <= MATURE_MAX:
    print('зрелость')

if OLD <= user_age:
    print('старость')