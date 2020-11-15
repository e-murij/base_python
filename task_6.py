products = []
analitic_dict = {'название': [],
                 'цена': [],
                 'количество': [],
                 'единица измерения': []
                 }
while True:
    user_answer = input('Выбирите действие:\n 1. Добавить товар\n 2. Посмотреть анализ\n '
                        '3. Посмотреть существующий список товаров\n 4. Для выхода нажмите q\n')
    if user_answer == '1':
        products.append((len(products) + 1, {'название': input('введите название товара: '),
                                             'цена': input('введите цену:'),
                                             'количество': input('введите количество: '),
                                             'единица измерения': input('введите единицу измерения: ')
                                             }
                         ))
    elif user_answer == '2':
        for i in range(len(products)):
            analitic_dict['название'].append(products[i][1]['название'])
            analitic_dict['цена'].append(products[i][1]['цена'])
            analitic_dict['количество'].append(products[i][1]['количество'])
            analitic_dict['единица измерения'].append(products[i][1]['единица измерения'])
        print(analitic_dict)
    elif user_answer == '3':
        print(products)
    elif user_answer == 'q':
        break
    else:
        print('Вы ввели неверную команду')
        continue
