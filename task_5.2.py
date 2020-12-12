# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open("task_5.2_data.txt", 'r', encoding='utf-8') as my_f:
        print(f'Всего строк - {len(my_f.readlines())}')
        my_f.seek(0)
        for i, line in enumerate(my_f, 1):
            print(f'{i}. Количиство символов в строке №{i} - {len(line)}')
            print(' '*2, f'Количиство слов в строке №{i}: {" ".join(line.split())} - {len(line.split())}')
except IOError:
    print('Произошла ошибка ввода-вывода')
