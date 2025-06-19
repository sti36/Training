"""Ровно в одном 1️⃣
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2. Функция должна возвращать значение True, если слова имеют одинаковую длину и отличаются одним символом на одной и той же позиции, или False в противном случае.

Примечание. Приведённый ниже код:

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
должен выводить:

True
True
False
False"""

# объявление функции
def is_one_away(word1, word2):
    count = 0  
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
    if count == 1:    
        return True
    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))