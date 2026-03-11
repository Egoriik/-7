import random
from collections import Counter

list = [random.randint(1,100) for _ in range(10)]
count = Counter(list)
duplicates = [i for i, cnt in count.items() if cnt>1]
if duplicates:
    print(f"Да, в списке есть повторяющиеся числа: {duplicates}")
else:
    print("Нет, в списке нет повторяющихся чисел")

print(f"Исходный список: {list}")