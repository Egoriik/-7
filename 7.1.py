import random

list = [random.randint(0,100) for i in range(5)]
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Вводите числа")

if num in list:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")


print(f"Изначальный список: {list}")
