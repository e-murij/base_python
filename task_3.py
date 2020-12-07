class IsNotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    user_input = input('Введите элемент списка или q для выхода и нажмите enter: ')
    if user_input.lower() == 'q':
        print(result_list)
        break
    try:
        if user_input.replace('.', '').replace('-', '').isdigit():
            result_list.append(float(user_input))
        else:
            raise IsNotNumber('Введено не число')
    except IsNotNumber as err:
        print(err)
