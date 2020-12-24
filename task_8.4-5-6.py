# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class OfficeEquipment:
    def __init__(self, title, price, quantity, units):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.units = units

    def __str__(self):
        return self.title


class Printer(OfficeEquipment):
    def __init__(self, title, price, quantity, units, is_colored, print_type):
        super().__init__(title, price, quantity, units)
        self.is_colored = is_colored
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, title, price, quantity, units, scan_type):
        super().__init__(title, price, quantity, units)
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    def __init__(self, title, price, quantity, units, speed):
        super().__init__(title, price, quantity, units)
        self.speed = speed


class Warehouse:
    def __init__(self, name):
        self.technics = []
        self.name = name

    def __str__(self):
        return f'Склад: {self.name} - {[str(i) for i in self.technics]}'

    def to_take(self, item):
        self.technics.append(item)


print('--Склад оргтехники--')

warehouse1 = Warehouse('Московский')

printer1 = Printer('Принтер черно-белый', 2500, 3, 'шт', True, 'Jet')
printer2 = Printer('Принтер цветной', 4500, 2, 'шт', True, 'Jet')
scanner1 = Scanner('Сканер 1', 1000, 1, 'шт', 'Планшетный')
scanner2 = Scanner('Сканер 2', 1500, 3, 'шт', 'Ручной')
xerox1 = Xerox('Ксерокс 1', 5500, 1, 'шт', 500)
xerox2 = Xerox('Ксерокс 2', 7000, 2, 'шт', 400)


warehouse1.to_take(printer1)
warehouse1.to_take(printer2)
warehouse1.to_take(scanner1)
warehouse1.to_take(scanner2)
warehouse1.to_take(xerox1)
warehouse1.to_take(xerox2)

print(warehouse1)