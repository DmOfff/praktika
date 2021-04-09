# Даны катеты прямоугольного треугольника. Найдите площадь, периметр и гипотенузу треугольника.

import math

c1 = int(input("катет a: "))
c2 = int(input("катет b: "))

print(f"Периметр: {round(math.sqrt(c1*c1 +c2*c2)+c1+c2)}")
print(f"Гипотенуза: {round(math.sqrt(c1*c1 +c2*c2))}")
print(f"Площадь: {round(0.5 * (c1 * c2), 2)}")


