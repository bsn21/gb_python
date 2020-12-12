# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open('task_5.1_data.txt', 'w', encoding='utf-8') as my_f:
        while True:
            content = input('Введите строку, для выхода просто нажмите Enter): ')
            if not content: # можно и так записать(=): if content == '':
                break
            my_f.write(content + '\n') # можно и так записать(=): my_f.write(f'{content}\n')
except IOError:
    print('Произошла ошибка ввода-вывода')