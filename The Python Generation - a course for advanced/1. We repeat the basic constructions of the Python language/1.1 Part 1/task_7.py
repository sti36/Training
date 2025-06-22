"""Standard American Convention
На вход программе подается натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подается натуральное число n(0<n<10^100).

Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи."""

number = int(input())

line = str(number)
list_number = []
list_number += line
list_number.reverse()

for i in range(3, len(list_number), 3):
    list_number[i] += ','

list_number.reverse()
print(*list_number, sep='')