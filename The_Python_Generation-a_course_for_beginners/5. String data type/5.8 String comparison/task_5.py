"""Сортируем слова 📶
На вход программе подаются 3 различных слова. Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.

Формат входных данных
На вход программе подаются 3 слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 3 слова на одной строке, разделяя их символом пробела."""

first_word = input()
second_word = input()
third_word = input()

min_word = min(first_word, second_word, third_word)
max_word = max(first_word, second_word, third_word)

if min_word != first_word != max_word:
    middle_word = first_word
elif min_word != second_word != max_word:
    middle_word = second_word
elif min_word != third_word != max_word:
    middle_word = third_word
    
print(min_word, middle_word, max_word)