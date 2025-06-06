"""YES or NO – вот в чём вопрос ❓
Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES» (без кавычек) либо «NO» (без кавычек).

Условия:

если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».
Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

number = int(input())

if (number % 2 != 0) or ((6 <= number <= 20) and number % 2 == 0):
    print('YES')
elif ((2 <= number <= 5) and number % 2 == 0) or (number > 20 and number % 2 == 0):
    print('NO')