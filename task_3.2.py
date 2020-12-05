# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

print('--1--')
# 1) Вариант - вывод в одну строчку, входные данные в print

def person_params(**kwargs):
    return ', '.join(kwargs.values())

print(person_params(имя=input('Ваше имя: '), фамилия=input('Ваша фамилию: '), \
                    год_рождения=input('Ваш год рождения: '), город_проживания=input('Ваш город проживания: '), \
                    email=input('Ваш e-mail: '), телефон=input('Ваш телефон: ')))

print('--2--')
# 2) Вариант - вывод в одну строчку через распаковку**, входные данные через словарь dict

def person_params(**kwargs):
    return '; '.join(kwargs.values())

params = {
    'имя': input('Ваше имя: '),
    'фамилия': input('Ваша фамилию: '),
    'год рождения': input('Ваш год рождения: '),
    'город проживания': input('Ваш город проживания: '),
    'email': input('Ваш e-mail: '),
    'телефон': input('Ваш телефон: ')
}

print(person_params(**params))

print('--3--')
# 3) Вариант - вывод в несколько строк, входные данные в print

def person_params(**kwargs):
    print('*' * 20,'\nДанные пользователя:')
    for key, value in kwargs.items():
        print(f'{key} - {value}')

person_params(имя=input('Ваше имя: '), фамилия=input('Ваша фамилию: '), год_рождения=input('Ваш год рождения: '), \
              город_проживания=input('Ваш город проживания: '), email=input('Ваш e-mail: '), \
              телефон=input('Ваш телефон: '))

print('--4--')
# 4) Вариант - вывод в одну строчку, входные данные указаны через параметры и print

def person_params(name, surname, birthday, city, email, phone):
    return f'Данные пользователя: Имя - {name}, Фамилия - {surname}, День рождения - {birthday}, '\
            f'Город проживания - {city}, Email -  {email}, Телефон - {phone}'

name = input('Ваше имя: ')
surname = input('Ваша фамилию: ')
birthday = input('Ваш год рождения: ')
city = input('Ваш город проживания: ')
email = input('Ваш e-mail: ')
phone = input('Ваш телефон: ')

print(person_params(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))