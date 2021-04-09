# Вывести 3 случайных числа от 0 до 100 без повторений.

import random

nums = []
for i in range(0, 3):
    n = random.randint(0, 100)
    if n in nums:
        while n not in nums:
            n = random.randint(0, 100)
        nums.append(n)
    else:
        nums.append(n)

print(nums)