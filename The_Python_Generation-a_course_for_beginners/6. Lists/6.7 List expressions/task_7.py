"""В одну строку 1
На вход программе подаётся строка текста, содержащая слова. Напишите программу, которая выводит слова введённой строки в столбик.

Формат входных данных
На вход программе подаётся строка текста, содержащая слова, разделённые символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Программу можно написать в одну строку кода."""

print(*input().split(), sep='\n')