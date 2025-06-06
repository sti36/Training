"""Третья цифра 3️⃣
Дано натуральное число number(number>99). Напишите программу, которая определяет его третью (с начала) цифру.

Формат входных данных 
На вход программе подаётся одно натуральное число, состоящее как минимум из трёх цифр.

Формат выходных данных
Программа должна вывести его третью (с начала) цифру."""

number = int(input())
one_digit = 0
two_digit = 0
three_digit = 0

while number != 0:
    three_digit = two_digit
    two_digit = one_digit
    one_digit = number % 10
    number //= 10
    
print(three_digit)