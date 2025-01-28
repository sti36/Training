"""Четырёхзначное число
Напишите программу для нахождения цифр четырёхзначного числа."""

number = int(input())

last_digit = number % 10
second_digit = (number % 100) // 10
third_digit = (number % 1000) // 100
fourth_digit = (number % 10000) // 1000

print('Цифра в позиции тысяч равна', fourth_digit)
print('Цифра в позиции сотен равна', third_digit)
print('Цифра в позиции десятков равна', second_digit)
print('Цифра в позиции единиц равна', last_digit)