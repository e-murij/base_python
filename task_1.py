class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def transformation(cls, data):
        try:
            day, month, year = map(int, data.split('-'))
            return cls(day, month, year)
        except ValueError:
            print('некорректно введены данные, день, год и месяц должны быть числами')

    @staticmethod
    def valid(obj):
        try:
            return True if (1 <= obj.day <= 31 and 1 <= obj.month <= 12 and 1 <= obj.year <= 9999) else False
        except AttributeError:
            return 'не могу проверить некорректные данные'


my_data = Data.transformation('32-10-2020')
print(Data.valid(my_data))
