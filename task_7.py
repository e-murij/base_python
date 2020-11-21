def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


def fact_gen(n):
    for el in range(1, n + 1):
        yield fact(el)


try:
    n = int(input('Введите целое неотрицательное число: '))
except ValueError:
    print('Ошибка ввода! Введите целое неотрицательное число')
else:
    if n < 0:
        print('Факториал определен только для неотрицательных чисел')
        exit()
    print('0! = 1')
    for ind, el in enumerate(fact_gen(n), 1):
        print(f'{ind}! = {el}')
