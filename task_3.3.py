# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print('--1--')
# 1) вариант - args, сумма трех чисел минус минимальное

def my_func(*args):
    a = sum(args)
    b = min(args)
    return a - b

print(my_func(200, 100, 300))


print('--2--')
# 2) вариант - args, похожий вариант
def my_func(*args):
    args = list(args)
    args.remove(min(args))
    return sum(args)

print(my_func(200, 100, 300))


print('--3--')
# 3) вариант - args, нахождение максимальных чисел в списке

def my_func(*args):
    args = list(args)
    m = max(args)
    args.remove(m)
    mm = max(args)
    return m + mm

print(my_func(200, 100, 300))

print('--4--')
# 4) вариант - сортировка args по убыванию и сложение args[0] и args[1].

def my_func(*args):
    args = sorted(args, reverse=True) # можно одной строкой return sum(sorted(args)[1:])
    return sum(args[:2])

print(my_func(200, 100, 300))

print('--5--')
# 5) вариант - lambda

my_func = lambda a, b, c: (a + b + c) - min(a, b, c)
print(my_func(200, 100, 300))

print('--6--')
# 6) вариант - аргументы, с исключениями и с input

def my_func(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
        my_list = [a, b, c]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return 'Ошибка, введите число'

a = input('Первое число: ')
b = input('Второе число: ')
c = input('Третье число: ')

print(my_func(a=a, b=b, c=c))


