"""Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Приведённый ниже код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
должен выводить:

[0, 4, 7, 8, 9]
[]
[4]"""

# объявление функции
def find_all(target, symbol):
    index_letter = 0   # Инициализируем переменную index_letter для отслеживания текущего индекса
    list = []  # Создаем пустой список list для хранения индексов символов
    for i in target:     # Проходим по каждому символу в строке target
        if i == symbol:  # Если текущий символ равен заданному символу
            list.append(index_letter)  # Добавляем текущий индекс index_letter в список list
        index_letter += 1           # Увеличиваем индекс index_letter на 1
    return list             # Возвращаем список индексов, где найден заданный символ

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))