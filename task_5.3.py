# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("task_5.3_salary.txt", 'r', encoding='utf-8') as my_f:

    workers_dict = {}
    for line in my_f:
        key = line.split()[0]
        value = float(line.split()[1])
        # теперь в словарь workers_dict для ключа key запишем значение value
        workers_dict[key] = value
    print(workers_dict)

    workers_list = []
    for key, value in workers_dict.items():
        if value < 20000:
            workers_list.append(key)
    print(f'Сотрудники, оклад котороых менее 20 тыс.: {", ".join(workers_list)}.')

    # те же сторудники, только через тернарный оператор:
    workers_list = [key for key, value in workers_dict.items() if value < 20000]
    print(f'Сотрудники, оклад котороых менее 20 тыс.: {", ".join(workers_list)}.')

    average_salary = round(sum(workers_dict.values()) / len(workers_dict), 2)
    print(f'Средняя величина дохода всех сотрудников = {average_salary}')
