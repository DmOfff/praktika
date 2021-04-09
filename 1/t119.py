# Найдите четырехзначные числа, сумма цифр которых равна 15.

def get_sum(x):
    summa = 0
    for n in str(x):
        summa += int(n)
    return summa


for i in range(1000, 9999):
    if get_sum(i) == 15:
        print(i)
