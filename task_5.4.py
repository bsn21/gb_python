# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

try:
    with open("task_5.4_numbers_ru.txt", 'w', encoding='utf-8') as my_file_ru:
        try:
            with open('task_5.4_numbers_eng.txt', 'r', encoding='utf-8') as my_file:
                for line in my_file:
                    eng_word = str(line.split()[0])
                    if eng_word in translate:
                        new_line = line.replace(eng_word, translate.get(eng_word))
                        my_file_ru.write(new_line)
        except IOError:
            print('Произошла ошибка ввода-вывода')
except IOError:
    print('Произошла ошибка ввода-вывода')
