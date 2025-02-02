"""Самописный калькулятор 🌶️
Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция» (без кавычек). Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек)."""

first_number, second_number, operator = int(input()), int(input()), input()

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == '/':
    if second_number == 0:
        print('На ноль делить нельзя!')
    else:
        print(first_number / second_number)
else:
    print('Неверная операция')