with open("text_3.txt", "r", encoding="utf-8") as f:
    employees_list = f.read().split('\n')
sum = 0
print(employees_list)
print('Зарплата меньше 20000:')
for el in employees_list:
    if float(el.split()[1]) < 20000:
        print(el.split()[0], end=' ')
    sum += float(el.split()[1])
print(f'\nСредняя зарпалата: {sum / len(employees_list)}')
