"""Угадайка слов
Описание проекта: программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова неизвестны. Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово. Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги).

Составляющие проекта:

Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл while;
Бесконечный цикл;
Операторы break, continue;
Создание пользовательских функций;
Списочные выражения;
Работа с модулем random для генерации случайных чисел.

Примечание 1. На английском игра называется Hangman."""

# Заголовок программы:
import random

word_list = ['математика', 'геометрия', 'информатика', 'программирование', 'питон', 'образование', 'телефон']

# функция получения случайного слова из списка слов
def get_word():
    word = random.choice(word_list)
    return word.upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Введите букву или слово целиком: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже называли букву', guess)
            elif guess not in word:
                print('Буквы', guess, 'нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Отличная работа, буква', guess, 'присутствует в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже называли слово', guess)
            elif guess != word:
                print('Слово', guess, 'не является верным.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')

again = 'д'

while again.lower() == 'д':
    word = get_word()
    play(word)
    again = input('Играем еще раз? (д = да, н = нет):')