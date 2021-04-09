# Дано две даты, каждая из которых состоит из трех чисел (день, месяц и год).
# Вывести yes, если первая дата раньше второй, иначе вывести no.

import datetime

d1 = datetime.datetime(int(input("Введите год: ")),
                       int(input("Введите месяц: ")),
                       int(input("Введите день: ")))

d2 = datetime.datetime(int(input("Введите год: ")),
                       int(input("Введите месяц: ")),
                       int(input("Введите день: ")))

if d1 < d2:
    print('yes')
else:
    print('no')