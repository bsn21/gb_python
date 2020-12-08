# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

# 1) Вариант

def salary():
    try:
        hours, rate_per_hour, bonus = argv[1:]
        print(f'Выработка в часах -', hours)
        print(f'Ставка в час -', rate_per_hour)
        print(f'Премия -', bonus)
        hours, rate_per_hour, bonus = int(hours), int(rate_per_hour), int(bonus)
        print(f'Заработная плата сотрудника = {(hours * rate_per_hour) + bonus}')
    except ValueError:
        print('Необходимо ввести три числа')
salary()

# 2) Вариант

def salary2():
    try:
        hours, rate_per_hour, bonus = map(float, argv[1:])
        print(f'Заработная плата = {(hours *rate_per_hour) + bonus}')
    except ValueError:
        print('Необходимо ввести три числа')

salary2()