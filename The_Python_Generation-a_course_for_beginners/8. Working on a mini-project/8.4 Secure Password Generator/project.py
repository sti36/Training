"""Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

Составляющие проекта:

Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл for;
Написание пользовательских функций;
Работа с модулем random для генерации случайных чисел.
"""

from random import choice

# функции на запрос данных у пользователя
def count():
    n = input('Сколько нужно паролей? Укажи цифру: ')
    while n.isdigit() == False:
        print('Нужно вводить цифу, дубина!')
        n = input('Сколько нужно паролей? Укажи цифру: ')
    return int(n)

def long():
    l = input('Введи длину пароля: ')
    while l.isdigit() == False:
        print('Нужно вводить цифу, дубина!')
        l = input('Введи длину пароля: ')
    return int(l)

def is_number():
    isn = input('Нужны ли в пароле цифры 0123456789? Напиши "да" или "нет": ')
    while isn.lower() not in ['да', 'нет']:
        print('Нужно вводить "да" или "нет".')
        isn = input('Нужны ли в пароле цифры 0123456789? Напиши "да" или "нет": ')
    return isn

def is_upper():
    isup = input('Нужны ли в пароле заглавные буквы? Напиши "да" или "нет": ')
    while isup.lower() not in ['да', 'нет']:
        print('Нужно вводить "да" или "нет".')
        isup = input('Нужны ли в пароле заглавные буквы? Напиши "да" или "нет": ')
    return isup

def is_lower():
    islw = input('Нужны ли в пароле строчные буквы? Напиши "да" или "нет": ')
    while islw.lower() not in ['да', 'нет']:
        print('Нужно вводить "да" или "нет".')
        islw = input('Нужны ли в пароле строчные буквы? Напиши "да" или "нет": ')
    return islw
    
def is_symbol():
    issmb = input('Нужны ли в пароле символы? Напиши "да" или "нет": ')
    while issmb.lower() not in ['да', 'нет']:
        print('Нужно вводить "да" или "нет".')
        issmb = input('Нужны ли в пароле символы? Напиши "да" или "нет": ')
    return issmb

def is_ambiguous():
    amb = input('Будут ли в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
    while amb.lower() not in ['да', 'нет']:
        print('Нужно вводить "да" или "нет".')
        amb = input('Могут ли быть в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
    return amb

# собираем возможные для пользователя символы в кучу
def gen_chars():
    chars = ''
    if isn == 'да':
        chars += '0123456789'
    if isup == 'да':
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if islw == 'да':
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if issmb == 'да':
        chars += '!#$%&*+-=?@^_'
    if amb == 'нет':
        for i in range(len(chars)):
            if chars[i] in 'il1Lo0O':
                del chars[i]
    return chars

# делаем пароли
def build_password():
    for i in range(n):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))
        
# старт программы
n = count()
l = long()
isn = is_number()            
isup = is_upper()
islw = is_lower()
issmb = is_symbol()
amb = is_ambiguous()
chars = gen_chars()
build_password()