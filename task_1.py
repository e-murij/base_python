import numpy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el_1) for el_1 in el]) for el in self.matrix]))

    def __add__(self, other):
        return numpy.array(self.matrix) + numpy.array(other.matrix)


matrix_1 = Matrix([[1, 2, 3], [3, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [3, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_1 + matrix_2)
