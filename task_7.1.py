# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, m_content=[[]]):
        self.m_content = m_content

    def __str__(self):
        result = ''
        for i in range(0, len(self.m_content)):
            for l in range(0, len(self.m_content[i])):
                result = result + str(self.m_content[i][l]) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        if len(self.m_content) == len(other.m_content) and len(
                self.m_content[0]) == len(other.m_content[0]):
            result = []
            for i_row in range(0, len(self.m_content)):
                temp_list = []
                for i_col in range(0, len(self.m_content[0])):
                    temp_list.append(self.m_content[i_row][i_col] +
                                other.m_content[i_row][i_col])

                result.append(temp_list)
            return Matrix(result)
        else:
            print('Матрицы разного размера')


matrix_1 = Matrix([[1, 1, 1], [3, 3, 3]])
matrix_2 = Matrix([[6, -2, 5], [2, -5, 2]])
print(matrix_1)
print(matrix_2)
result_matrix = matrix_1 + matrix_2
print(result_matrix)