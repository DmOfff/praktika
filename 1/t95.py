# Даны a и n. Вычислите p=(a+1)^2*(a+2)^2⋅…⋅(a+n)^2

import math

a = int(input("a: "))
n = int(input("n: "))
summa = 1

for i in range(1, n+1):
    summa *= math.pow(a + i, 2)

print(summa)