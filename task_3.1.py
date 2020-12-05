# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_divide(a, b):
    try:
        a, b = int(a), int(b)
        result = a / b
    except ZeroDivisionError:
        return 'ZeroDivisionError - Ошибка! Нельзя делить на ноль'
    except ValueError:
        return 'ValueError - Ошибка! Необходимо ввести число'
    except:
        return 'Неизвестная ошибка'
    return round(result, 2)

print(my_divide(input('Введите первое число: '), input('Введите первое число: ')))
