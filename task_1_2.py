with open("text_1.txt", "w+", encoding="utf-8") as f:
    print('Введите данные:')
    while str:
        str = input()
        print(str, file=f)
    f.seek(0)
    content = f.readlines()
print(f'Количество строк: {len(content)}')
for ind, el in enumerate(content, 1):
    print(f'Количество слов в {ind} строке: {len(el.split())}')
