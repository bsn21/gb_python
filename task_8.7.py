# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class NumComplex:
    def __init__(self, clx):
        self.clx = clx

    def __add__(self, other):
        return self.clx + other.clx

    def __mul__(self, other):
        return self.clx * other.clx

    def __str__(self):
        return str(self.clx)


complex1 = NumComplex(-2 + 5j)
complex2 = NumComplex(15 + 9j)
print(complex1, complex2)

print(f'{complex1} + {complex2} = {complex1 + complex2}')
print(f'{complex1} * {complex2} = {complex1 + complex2}')
