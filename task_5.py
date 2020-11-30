class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Инстумент {self.title} запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Инстумент {self.title} запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Инстумент {self.title} запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Инстумент {self.title} запуск отрисовки маркером')


stationery = Stationery('базовый')
stationery.draw()
pen = Pen('красная ручка')
pen.draw()
pencil = Pencil('твердый карандаш')
pencil = pencil.draw()
hendle = Handle('зеленый маркер')
hendle.draw()
