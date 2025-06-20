"""Корни уравнения 🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c=0 и возвращает его корни в порядке возрастания.

Примечание 1. С подобной задачей мы уже сталкивались.

Примечание 2. Гарантируется, что квадратное уравнение имеет хотя бы один корень.

Примечание 3. Приведённый ниже код:

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
должен выводить:

-1.0 5.0
1.0 2.5
-1.0 -1.0
Примечание 4. Если уравнение имеет только один корень, нужно вернуть два числа, равных этому корню."""

# Объявление функции для решения квадратного уравнения
def solve(a, b, c):
    d = b ** 2 - 4 * a * c  # Вычисляем дискриминант
    
    # Вычисляем два корня уравнения
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    
    return min(x1, x2), max(x1, x2)  # Возвращаем корни в порядке возрастания

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)

print(x1, x2)