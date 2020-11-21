import random

start_list = [random.randint(1, 20) for i in range(0, 20)]
new_list = [el for el in start_list if start_list.count(el) == 1]
print(start_list)
print(new_list)
