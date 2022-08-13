# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random
numbers = []

n = int(input())
i = 0
w = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)
for num in numbers:
    if num > 0 and num % 2 == 0:
        w = w + num
print(w)
