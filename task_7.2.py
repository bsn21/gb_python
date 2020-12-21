# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def count_consumption(self):
        pass


class Coat(AbstractClothes):
    def count_consumption(self):
        return self.param / 6.5 + 0.5


class Suit(AbstractClothes):
    def count_consumption(self):
        return (self.param * 2 + 0.3) / 100


class FabricConsumption:
    def __init__(self):
        self.consumption = 0

    def add_coat(self, name, param):
        coat = Coat(name, param)
        self.consumption += coat.count_consumption()

    def add_suit(self, name, param):
        suit = Suit(name, param)
        self.consumption += suit.count_consumption()

    @property
    def count_consumption(self):
        return self.consumption


my_fabric_consumption = FabricConsumption()
my_fabric_consumption.add_coat('Kate', 42)
my_fabric_consumption.add_suit('Alexander', 184)
print(f'Общий расход ткани = {round(my_fabric_consumption.count_consumption, 2)} м')