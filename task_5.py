import random

data_list = [str(random.randint(1, 10)) for _ in range(0, 5)]
with open("text_5.txt", "w+", encoding="utf-8") as f:
    f.write(' '.join(data_list))
    f.seek(0)
    numbers = list(map(int, f.read().split()))
print(numbers)
print(f'Сумма чисел в файле: {sum(numbers)}')
