# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    print('--Деление чисел--')
    num1 = int(input('Введите число № 1: '))
    num2 = int(input('Введите число № 2: '))
    if num2 == 0:
        raise MyZeroDivision('Деление на ноль недопустимо!')
except MyZeroDivision as err:
    print(err.msg)
else:
    print(f'{num1} / {num2} = {num1 / num2}')