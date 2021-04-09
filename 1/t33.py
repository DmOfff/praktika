# Вычислите √(x−√(y)), если x и y вводит пользователь.
# Перед вычислением выполнить проверку на существование квадратных корней.

import math


def has_koren(x):
    if math.sqrt(x) * math.sqrt(x) == x:
        return True
    return False


x = int(input("x: "))
y = int(input("y: "))

if not has_koren(x):
    print("x не имеет квадратного корня")

if not has_koren(y):
    print("y не имеет квадратного корня")

print(f"√({x}−√({y}))={math.sqrt(x - math.sqrt(y))}")
