departament_list = ['Общий склад', 'Производственный отдел', 'Бухгалтерия', 'Административный отдел']


class MyExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.xerox = []
        self.printer = []
        self.scanner = []

    def add_technics(self, a):
        name = input('Введите название устройства:\n')
        try:
            quantity = int(input('Введите количество:\n'))
            if quantity < 0:
                raise MyExeption('Количество не может быть отрицательным')
        except ValueError:
            print('Количество должно быть целым положительным числом')
        except MyExeption as arr:
            print(arr)
        else:
            if a == '1':
                color = bool(input('Если принтер цветной введите любой символ, если черно белый нажмите enter\n'))
                self.printer.append(Printer(name, quantity, color))
            elif a == '2':
                network = bool(input('Если сканер сетевой введите любой символ, если нет нажмите enter\n'))
                self.scanner.append(Scaner(name, quantity, network))
            elif a == '3':
                a3_support = bool(
                    input('Если ксерокс поддерживает формат А3 введите любой символ, если нет нажмите enter\n'))
                self.xerox.append(Printer(name, quantity, a3_support))

    def print_technics(self, a):
        if a == '1':
            if not self.printer:
                print('На складе нет принтеров')
            else:
                for ind, el in enumerate(self.printer, 1):
                    print(f'{ind}. {el}')
        elif a == '2':
            if not self.scanner:
                print('На складе нет сканеров')
            else:
                for ind, el in enumerate(self.scanner, 1):
                    print(f'{ind}. {el}')
        elif a == '3':
            if not self.xerox:
                print('На складе нет ксерокса')
            else:
                for ind, el in enumerate(self.xerox, 1):
                    print(f'{ind}. {print(el)}')

    def move_technics(self, a):
        for ind, el in enumerate(departament_list, 1):
            print(f'{ind} {el}')
        try:
            new_dep = departament_list[int(input('Выберите отдел в который будет передано устройство:\n')) - 1]
        except IndexError:
            print('Такого отдела нет\n')
        else:
            storage.print_technics(a)
            try:
                unit = int(input('Выбери устройство:\n'))
                if a == '1':
                    self.printer[unit - 1].unit['отдел'] = new_dep
                if a == '2':
                    self.scanner[unit - 1].unit['отдел'] = new_dep
                if a == '3':
                    self.xerox[unit - 1].unit['отдел'] = new_dep
            except (IndexError, ValueError):
                print('Такого устройства нет')


class Technics:
    def __init__(self, name, quantity, department=departament_list[0]):
        self.unit = {'Название': name, 'отдел': department, 'количество': quantity}

    def __str__(self):
        return f'{self.unit}'.replace('{', '').replace('}', '').replace("'", '')


class Printer(Technics):
    def __init__(self, name, quantity, color=False):
        super().__init__(name, quantity)
        self.unit['цветной'] = color


class Scaner(Technics):
    def __init__(self, name, quantity, network=False):
        super().__init__(name, quantity)
        self.unit['работает по сети'] = network


class Xerox(Technics):
    def __init__(self, name, quantity, a3_support=False):
        super().__init__(name, quantity)
        self.unit['формат А3'] = a3_support


storage = Storage()
while True:
    menu = input(
        'Выберите пункт меню:\n'
        '1.Добавить устройство\n'
        '2.Вывести список существующих устройств\n'
        '3.Переместить устройство в другой отдел\n'
        '4.Выход\n'
    )
    if menu == '4':
        exit()
    elif menu == '1':
        a = input('Выберите тип устройства:\n1.Принтер\n2.Сканер\n3.Ксерокс\n')
        print('Такого варианта нет\n') if a < '1' or a > '3' else storage.add_technics(a)
    elif menu == '2':
        a = input('Выберите тип устройства:\n1.Принтер\n2.Сканер\n3.Ксерокс\n')
        print('Такого варианта нет\n') if a < '1' or a > '3' else storage.print_technics(a)
    elif menu == '3':
        a = input('Выберите тип устройства:\n1.Принтер\n2.Сканер\n3.Ксерокс\n')
        print('Такого варианта нет\n') if a < '1' or a > '3' else storage.move_technics(a)
