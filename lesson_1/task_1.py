# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные,выведите на экран.

name = input("What's your name? ")
print("Hello, ", name)
number = int(input("Еnter an integer: "))
print("number/2 = ", number / 2)
print("number*2 = ", number * 2)
print("number+2 = ", number + 2)
print("number-2 = ", number - 2)
print("number to the power of 3 = ", number ** 3)
remainder = number % 3
print("remainder of division by 3 = ", remainder, type(remainder))
number = float(number)
print(number, type(number))
