"""Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надёжным, или False в противном случае.

Пароль является надёжным, если:

его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
Примечание. Приведённый ниже код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:

True
False"""

MIN_LEN_PASSWORD = 8

# объявление функции
def is_password_good(password):
    if len(password) < MIN_LEN_PASSWORD:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3 

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))