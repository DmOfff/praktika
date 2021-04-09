# Назовем автобусный билет несчастливым, если сумма цифр его шестизначного номера делится на 13. Могут ли два идущих подряд билета оказаться несчастливыми?
import random

x = random.randint(1000000000000000, 9999999999999998)


def get_nums_sum(n):
    summa = 0
    for i in str(n):
        summa += int(i)
    return summa


sum_1 = get_nums_sum(x)
sum_2 = get_nums_sum(x + 1)

print(f"Билет номер 1({x}) счастливый" if sum_1 % 16 == 0 else f"Билет номер 1({x}) несчастливый")
print(f"Билет номер 2({x + 1}) счастливый" if sum_2 % 16 == 0 else f"Билет номер 2({x + 1}) несчастливый")