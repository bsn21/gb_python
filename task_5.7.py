# 7. Создать (не программно) текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

try:
    with open("task_5.7_firms.json", 'w', encoding='utf-8') as my_f_wj:
        try:
            with open("task_5.7_firms.txt", 'r', encoding='utf-8') as my_f_rt:
                all_profit, all_loss = [], []
                all_profit_dict = {}
                for line in my_f_rt:
                    firm = line.split()[0]
                    form = line.split()[1]
                    firm_list = line.split()
                    # print(firm_list)
                    profit = int(firm_list[2]) - int(firm_list[3])
                    if profit > 0:
                        # print(f'Прибыль {form} {firm}: {profit}')
                        all_profit.append(profit)
                    else:
                        # print(f'Убыток {form} {firm}: {profit}')
                        all_loss.append(abs(profit))
                    key = line.split()[0]
                    value = profit
                    all_profit_dict[key] = value
                average_profit = round(sum(all_profit) / len(all_profit), 2)
                average_loss = round(sum(all_loss) / len(all_loss), 2)
                # print(f'Средняя прибыль: {average_profit}', f'\nСредний убыток: {average_loss}')
                # print(all_profit_dict)
                result = [all_profit_dict, {'Средняя прибыль': average_profit}, {'Средний убыток': average_loss}]
                # print(result)
            json.dump(result, my_f_wj, ensure_ascii=False, indent=4)
        except IOError:
            print('Произошла ошибка ввода-вывода')
except IOError:
    print('Произошла ошибка ввода-вывода')
