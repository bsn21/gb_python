# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial

print('--1--')
# 1) вариант - с использованием math

def fact():
    for el in count(1):
        yield factorial(el)

my_generator = fact()
print(my_generator)
n = 0

for i in my_generator:
    if n == 15:
        break
    else:
        n += 1
        print(f'Факториал {n}! = {i}')

print('--2--')
# 2) вариант через range c input

def fact(n):
    result = 1
    if n == 0:
        yield f'Факториал {n}! = {result}'
    for el in range(1, n + 1):
        result *= el
        yield f'Факториал {el}! = {result}'

for i in fact(int(input('Введите число: '))):
    print(i)

print('--3--')
# 3) вариант - без input

def fact(n):
    result = 1
    if n == 0:
        yield result
    for el in range(1, n + 1):
        result *= el
        yield result

my_generator = fact(4)

for i in my_generator:
    print(i)