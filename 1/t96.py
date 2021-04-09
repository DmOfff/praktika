# Дано натуральное число n. Вычислите 1/cosx + 1/cosx^2 + …+1/cosx^n

import math

n = int(input('n: '))
x = int(input('x: '))

sum = 0
for i in range(1, n+1):
    sum += 1 / math.cos(math.pow(x, n))

print(round(sum, 2))