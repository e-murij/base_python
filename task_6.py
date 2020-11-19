def int_func(text):
    return chr(ord(text[0]) - 32) + text[1:]  # вместо text.capitalize()


def string_sort(user_string_list):
    for word in user_string_list:
        for symbol in word:
            if ord(symbol) > 122 or ord(symbol) < 97:
                break
        else:
            print(int_func(word), end=' ')


user_string_list = input('введите строку: ').split()
string_sort(user_string_list)
