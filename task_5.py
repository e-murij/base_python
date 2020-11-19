def sum_string():
    flag = True
    total_sum = 0
    while flag:
        current_sum = 0
        number_list = input('введите числа, разделенные пробелом или q если хотите выйти: ').split()
        if 'q' in number_list:
            number_list = number_list[0:number_list.index('q')]
            flag = False
        try:
            number_list = [float(el) for el in number_list]
        except ValueError:
            print('Ошибка ввода. Строка должна содержать числовые значения либо спецсимвол "q" для выхода')
        else:
            current_sum = sum(number_list)
            total_sum += current_sum
            print(f'Сумма чисел текущей строки: {current_sum}\nОбщая сумма: {total_sum}')


sum_string()
