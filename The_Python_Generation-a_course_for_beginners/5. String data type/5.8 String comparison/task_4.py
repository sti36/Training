"""Необычное сравнение 📊
На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно, не учитывая регистр и игнорируя все небуквенные символы. Программа должна вывести «YES» (без кавычек), если строки окажутся равны в результате такой проверки, или «NO» (без кавычек) в противном случае.

Формат входных данных
На вход программе подаются 2 строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи."""

first_line = input()
second_line = input()

first_line_letters = ''
second_line_letters = ''

for s in first_line:
    if s.isalpha():
        first_line_letters += s.lower()

for s in second_line:
    if s.isalpha():
        second_line_letters += s.lower()

if first_line_letters == second_line_letters:
    print('YES')
else:
    print('NO')