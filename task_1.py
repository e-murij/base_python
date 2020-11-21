import sys


def pay(hours, hour_rate, prize):
    return hours * hour_rate + prize


try:
    print(pay(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
except IndexError:
    print('Недостаточно параметров. Необходимо ввести количество часов , ставку часа и премию')
except ValueError:
    print('Параметры должны быть числами')
