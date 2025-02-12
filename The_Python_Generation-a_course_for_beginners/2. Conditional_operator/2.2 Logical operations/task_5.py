"""Неравенство треугольника
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами."""

side_a, side_b, side_c = int(input()), int(input()), int(input())

if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
    print('YES')
else:
    print('NO')