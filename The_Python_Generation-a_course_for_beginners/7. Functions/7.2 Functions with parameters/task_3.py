"""Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр."""

# объявление функции
def print_digit_sum(num):
    total = sum(int(digit) for digit in str(num))
    print(total)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)