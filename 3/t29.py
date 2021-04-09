# Дан массив x из n элементов. Найдите X1 - X2 + X3 - ... - Xn-1 + Xn

n = int(input('n: '))

x = []
for i in range(1, n+1):
    x.append(i)

summa = 0
for index, i in enumerate(x):
    if index % 2 == 0:
        summa += i
    else:
        summa -= i

print(summa)
