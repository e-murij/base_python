import random

start_list = [random.randint(1, 100) for i in range(0, 20)]
new_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i - 1] < start_list[i]]
print(start_list)
print(new_list)
