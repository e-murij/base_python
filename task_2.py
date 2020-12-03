from abc import ABC, abstractmethod


class Сlothes(ABC):
    @abstractmethod
    def calculation_fabric(self):
        pass


class Coat(Сlothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculation_fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Сlothes):
    def __init__(self, height):
        self.height = height

    @property
    def calculation_fabric(self):
        return self.height * 2 + 0.3

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            self.__height = 100
        elif height > 200:
            self.__height = 200
        else:
            self.__height = height


sum_coat = sum([Coat(int(input('Размер: '))).calculation_fabric for _ in range(int(input('Количество пальто: ')))])
print(
    'Если рост больше 200, то расчет расхода ткани на костюм будет производиться на рост 200, если меньше 100, то на рост 100')
sum_suit = sum([Suit(int(input('Рост: '))).calculation_fabric for _ in range(int(input('Количество костюмов: ')))])
print(f'Необходимое количество ткани: {sum_coat + sum_suit:.4f}')
