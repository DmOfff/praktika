# Найдите сумму квадратов первых n натуральных чисел

n = int(input("n: "))
sum = 0

for i in range(1, n+1):
    sum += i * i

print(sum)