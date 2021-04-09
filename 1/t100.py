# Вывести на экран числа от 1000 до 9999 такие, что среди цифр нет цифр 5 и цифры 6


for i in range (1000,9999+1):
    x = list(str(i))
    if len(x) == len(set(x)):
        if "6" not in x and "5" not in x:
            print(i)