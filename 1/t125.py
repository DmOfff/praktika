# Вычислите значения функции f(x)=x2−sinx на отрезке [a;b] с шагом h. Результат представить в виде таблицы.

import math

a = int(input("a: "))
b = int(input("b: "))
h = int(input("h: "))

for i in range(a, b+h, h):
    print(f"f({i})={round(i * i - math.sin(i), 2)}")
