"""Дополнительная
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):"""

number = int(input())
list_numbers = [[0] * number for i in range(number)]
x = 0
y = 0

for i in range(1, number**2 + 1):
    list_numbers[x][y]=i
    if x <= y + 1 and x + y < number -1: y += 1
    elif x < y : x += 1
    elif x + y >= number : y -= 1
    elif x >= y : x -= 1
for i in range(number):
    print(* list_numbers[i])