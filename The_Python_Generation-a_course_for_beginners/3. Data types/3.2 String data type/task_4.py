"""Три города 🏙️
Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаются названия трёх городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трёх городов различны."""

first_city, second_city, third_city = input(), input(), input()

min_city_len = min(len(first_city), len(second_city), len(third_city))
max_city_len = max(len(first_city), len(second_city), len(third_city))

if len(first_city) == min_city_len:
    print(first_city)
elif len(second_city) == min_city_len:
    print(second_city)
else:
    print(third_city)

if len(first_city) == max_city_len:
    print(first_city)
elif len(second_city) == max_city_len:
    print(second_city)
else:
    print(third_city)