# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
rating = [7, 5, 3, 3]
while True:
    user_rating = input('Введите новый элемент рейтинга. Для выхода нажмите q: ')
    if user_rating == 'q':
        break
    if not user_rating.isdigit():
        print('некорректный ввод')
        continue
    user_rating = float(user_rating)
    lengh_raiting = len(rating)
    if user_rating <= rating[lengh_raiting - 1]:
        rating.insert(lengh_raiting, user_rating)
        print(rating)
        continue
    for i in range(lengh_raiting - 2):
        if user_rating > rating[i]:
            rating.insert(i, user_rating)
            break
    print(rating)
