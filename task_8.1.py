# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class DateError(Exception):
    def __init__(self, err):
        self.err = err


class Date:
    def __init__(self, date: str):
        self.day, self.month, self.year = self.date_parse(date)

    @classmethod
    def date_parse(cls, date: str):
        date_list = [int(i) for i in date.split('-')]
        try:
            if len(date_list) != 3:
                raise DateError('Формат даты должен быть: «день-месяц-год»')
            if cls.date_valid(date_list):
                return date_list
            else:
                raise DateError('Проверьте правильность введенной даты!')
        except DateError as err:
            print(err.err)

    @staticmethod
    def date_valid(date: list):
        if 1 <= date[0] <= 31 and 1 <= date[1] <= 12 and 1 <= date[2] <= 2020:
            return True
        else:
            return False

    def __str__(self):
        if self.day and self.month and self.year:
            return f'{self.day:02}.{self.month:02}.{self.year}'
        else:
            return 'Введены некоректные данные!'


my_date = Date('24-12-2020')
print(my_date)
print(my_date.date_parse('24-12-2020'))
print(my_date.date_parse('12-24-2020'))



