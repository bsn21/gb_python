# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# 1.1) вариант, где ввод одного слова с делением на 2

my_list = list(input('Напишите ваш любимый фрукт: '))

for i in range(len(my_list) // 2):  # можно и так - for el in range(int(len(my_list) / 2)): но это длиннее
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(''.join(my_list))

# 1.2) вариант, где ввод одного слова с шагом

my_list = list(input('Напишите ваш любимый фрукт: '))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(''.join(my_list))

# 2.1) вариант, где ввод нескольких слов с for с делением на 2

my_list = input('Напишите несколько любимых фруктов (через пробел): ').split()

for i in range(len(my_list) // 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(' '.join(my_list))

# 2.2) вариант, где ввод нескольких слов с while

my_list = input('Напишите несколько любимых фруктов (через пробел): ').split()

i = 0

while i + 1 < len(my_list):
    if i % 2 == 0:
        my_list.insert(i, my_list.pop(i + 1))
    i += 1

print(' '.join(my_list))

# 2.3) вариант, где ввод нескольких слов с for

my_list = input('Напишите несколько любимых фруктов (через пробел): ').split()

for i in range(1, len(my_list), 2):
    my_list.insert(i - 1, my_list.pop(i))

print(' '.join(my_list))