class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростю {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print('превышение скорости') if self.speed > 60 else print(
            f'{self.name} едет с допустимой скоростю {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        print('превышение скорости') if self.speed > 40 else print(
            f'{self.name} едет с допустимой скоростю {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def police(self):
        print('полицейская машина') if self.is_police else print('неправльная полицейская машина')


trakctor = WorkCar(60, 'желтый', 'трактор')
print(trakctor.color, trakctor.name)
trakctor.show_speed()
trakctor.turn('налево')
trakctor.speed = 30
trakctor.show_speed()
print()
police = PoliceCar(60, 'белый', 'ВАЗ', True)
print(police.color, police.name)
police.show_speed()
police.stop()
police.police()
