"""Next Prime 🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число, большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Приведённый ниже код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17"""

def is_prime(num):
    if num == 1:
        return False  # число 1 не является простым

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель

    return True


# объявление функции
def get_next_prime(num):
    cur_num = num + 1  # начинаем искать следующее простое число

    while not is_prime(cur_num):  # если следующее число непростое, то увеличиваем на 1
        cur_num += 1

    return cur_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))