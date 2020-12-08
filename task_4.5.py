# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

# 1) вариант - с помощью def
my_list = [el for el in range(100, 1001) if el % 2 == 0]
# можно через шаг:
# my_list = [el for el in range(100, 1001, 2)]

def my_func(a, b):
    return a * b

print(f'Произведение чисел:\n{reduce(my_func, my_list)}')

# 2) вариант - тоже самое, но с помощью lambda
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda a, b: a * b, my_list))

# 3) вариант - в одну строку
print(reduce(lambda a, b: a * b, [el for el in range(100, 1001) if el % 2 == 0]))
