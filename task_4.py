dict_rus = {'One': 'один',
            'Two': 'два',
            'Three': 'три',
            'Four': 'четыре'
            }
russian = []
with open("text_4.txt", "r", encoding="utf-8") as f:
    for line in f:
        word = line.split(' ', 1)
        try:
            russian.append(dict_rus[word[0]] + word[1])
        except KeyError:
            print(f'Слова {word[0]} нет в словаре')

with open("text_4_1.txt", "w", encoding="utf-8") as f:
    f.writelines(russian)
