# Дан массив из n элементов. Переставьте его элементы случайным образом.

import random

nums = []
n = int(input("n: "))

for i in range(n):
    nums.append(i)

random.shuffle(nums)

print(nums)