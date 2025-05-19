"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми."""

with open('dataset_3363_3.txt') as in_file:
    line = in_file.read().strip().lower().split()

max_count = 0
max_string = ''

for s in line:
    if line.count(s) > max_count or (line.count(s) == max_count and s < max_string):
        max_string = s
        max_count = line.count(s)

out = str(max_string) + ' ' + str(max_count)

with open('reply_3363_3.txt', 'w') as out_file:
    out_file.write(out)

print('Program is complete.', 'The most frequent word found!', sep='\n')