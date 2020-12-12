# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from typing import List

print('**1**')

# 1) вариант - запись чисел пользователем
try:
    with open("task_5.5_sum_num1.txt", 'w+', encoding='utf-8') as my_f:
        try:
            my_f.write(input('Введите набор чисел через пробелы: '))
            my_f.seek(0)
            sum_num = sum(map(int, my_f.readline().split()))
            print(f'Сумма всех введенных чисел = {sum_num}')
        except ValueError:
            print('Ошибка - необхдимо ввести число.')
except IOError:
    print('Произошла ошибка ввода-вывода')

print('\n**2**')

# 2) вариант - запись чисел randint
from random import randint

try:
    with open("task_5.5_sum_num2.txt", 'w+', encoding='utf-8') as my_f:
        my_f.write(' '.join(str(randint(1, 100)) for n in range(50)))
        my_f.seek(0)
        sum_num = sum(map(int, my_f.readline().split()))
        print(f'Сумма всех введенных чисел = {sum_num}')
except IOError:
    print('Произошла ошибка ввода-вывода')
