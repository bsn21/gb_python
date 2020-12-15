# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
import self as self


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'{self.name} повернула налево')
        else:
            print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч')

class TownCar(Car):

    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч: Превышена скорость!')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч')


class SportCar(Car):

    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):

    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч: Превышена скорость!')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч')

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar('"Lexus"', 'белый', 65)
sport_car = SportCar('"Audi"', 'красный', 150)
work_car = WorkCar('"Lada"', 'серый', 60)
police_car = PoliceCar('"Ford"', 'синий', 55)
town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
print(f'Цвет {sport_car.name} - {sport_car.color}')
police_car.go()
police_car.turn('left')
police_car.turn('')
police_car.stop()
print(f'{police_car.name} - полицейская машина: {police_car.is_police}')
print(f'{work_car.name} - полицейская машина: {work_car.is_police}')
