# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
proceeds = float(input("enter proceeds: "))
costs = float(input("enter costs: "))
if costs > proceeds:
    print("the company is operating at a loss")
elif costs == proceeds:
    print("the company works at zero")
else:
    print("the company works with profit")
    print(f'profitability = {(proceeds - costs) / proceeds:.3f}')
    employees = int(input("the number of employees: "))
    print(f'profit per one employee: {(proceeds - costs) / employees:.3f}')
