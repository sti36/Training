"""Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа."""

first_number, second_number = float(input()), float(input())
operation = input()

second_number_flag_null = False
if second_number != 0: #Проверка второго числа на 0
    second_number_flag_null = True

if operation == '+': #Операция сложения
    print(first_number + second_number)

elif operation == '-': #Операция вычитания
    print(first_number - second_number)

elif operation == '/' and second_number_flag_null == True: #Операция деления с остатком
    print(first_number / second_number)

elif operation == '*': #Операция умножения
    print(first_number * second_number)

elif operation == 'mod' and second_number_flag_null == True: #Операция взятия остатка от деления
    print(first_number % second_number)

elif operation == 'pow': #Операция возведения в степень
    print(first_number ** second_number)

elif operation == 'div' and second_number_flag_null == True: #Операция целочисленного деления
    print(first_number // second_number)

elif (operation == '/' or operation == 'div' or operation == 'mod') and second_number_flag_null == False: #Деление на 0
    print('Деление на 0!')