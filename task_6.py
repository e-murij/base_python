from itertools import count, cycle


def my_func(a, b, c):
    el_count = count(a, c)
    el_cycle = cycle([1, 'a', False])
    for i in range(0, b):
        print(f'{next(el_count)} : {next(el_cycle)}')


try:
    user_data = [int(el) for el in input('Введите начальное значение, количество итераций, шаг через пробел. ').split()]
    my_func(user_data[0], user_data[1], user_data[2])
except (ValueError, IndexError):
    print('ошибка ввода данных')
