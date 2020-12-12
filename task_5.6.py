# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

try:
    with open("task_5.6_subjects.txt", 'r', encoding='utf-8') as my_f:
        subject_dict = {}
        for line in my_f:
            key, params = line.split(':')
            params_num_list = []
            idx = 0
            while idx < len(params):
                params_num = ''
                el = params[idx]
                while '0' <= el <= '9':
                    params_num += el
                    idx += 1
                    if idx < len(params):
                        el = params[idx]
                    else:
                        break
                idx += 1
                if params_num != '':
                    params_num_list.append(int(params_num))
            value = sum(params_num_list)
            subject_dict[key] = value
        print(subject_dict)
except IOError:
    print('Произошла ошибка ввода-вывода')