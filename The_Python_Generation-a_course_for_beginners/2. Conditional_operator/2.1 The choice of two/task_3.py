"""Соотношение 
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр."""

number = int(input())

fourth_digit = number % 10
third_digit = (number % 100) // 10
second_digit = (number % 1000) // 100
first_digit = (number % 10000) // 1000

if first_digit + fourth_digit == second_digit - third_digit:
    print('ДА')
else:
    print('НЕТ')