# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    return (num_1 + num_2 + num_3) - min(num_1, num_2, num_3)


try:
    numbers = [float(input('введите число: ')) for i in range(0, 3)]
    print(my_func(numbers[0], numbers[1], numbers[2]))
except ValueError:
    print('Ошибка ввода. Вы ввели не числовое значение')
