"""Роскомнадзор 🔞
Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет."""

user_age = int(input())

if user_age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')