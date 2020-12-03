class Cell:
    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        return self.cells_number - other.cells_number if self.cells_number > other.cells_number else f'Ошибка вычитания'

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __floordiv__(self, other):
        try:
            return Cell(self.cells_number // other.cells_number)
        except ZeroDivisionError:
            return 'Ошибка деления, деление на 0'

    def make_order(self, count):
        result = ''
        for i in range(self.cells_number // count):
            result += ('*' * count) + '\n'
        result += ('*' * (self.cells_number % count))
        return result

    def __str__(self):
        return str(self.cells_number)


cell_1 = Cell(12)
cell_2 = Cell(46)
print(cell_2 - cell_1)
print(cell_1 - cell_2)
print(cell_1 + cell_2)
print(cell_2 // cell_1)
print(cell_2 * cell_1)
print(cell_2.make_order(10))
