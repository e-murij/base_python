import json

proseeds_dict = {}
count = 0
average_profit = 0
with open("text_7.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, form, proceeds, costs = line.split()
        proseeds_dict[name] = float(proceeds) - float(costs)
for val in proseeds_dict.values():
    if val > 0:
        average_profit += val
        count += 1
try:
    average_profit = average_profit / count
except ZeroDivisionError:
    print('Все фирмы работали с убытком')
list = [proseeds_dict, {'average_profit': average_profit}]

with open("text_77.json", "w", encoding="utf-8") as f:
    json.dump(list, f, indent=4, ensure_ascii=False)
