class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a}+{self.b}*i' if self.b > 0 else f'{self.a}{self.b}*i'


try:
    x = ComplexNumber(3, 1)
    y = ComplexNumber(2, -3)
    print(x + y)
    print(x * y)
except TypeError:
    print('некорректно введены данные')
