"""Алфавит
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат входных данных
На вход программе ничего не подаётся.

Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка должен состоять из 26 символов z."""

list = []

for i in range(26):
    cur = ""
    for j in range(i + 1):
        cur += chr(ord("a") + i)
    
    list.append(cur)

print(list)