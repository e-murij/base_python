class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


kate = Position('Kate', 'Smith', 'teacher', 100002, 30001)
print(kate.position)
print(kate.get_full_name())
print(kate.get_total_income())
