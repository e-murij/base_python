class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el_1) for el_1 in el]) for el in self.matrix]))

    def __add__(self, other):
        matrix_sum = []
        for sublist in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            matrix_sum.append(temp)
        return Matrix(matrix_sum)


matrix_1 = Matrix([[1, 2, 3], [3, 5, 6], [6, 1, 2]])
matrix_2 = Matrix([[1, 2, 3], [3, 5, 6], [9, 2, 5]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)
