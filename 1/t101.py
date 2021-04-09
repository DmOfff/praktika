# Вывести все пятизначные числа, которые делятся на 2,
# у которых средняя цифра нечетная, и сумма всех цифр делится на 4.

def mid(s, offset, amount):
    return s[offset:offset + amount]


for i in range(10000, 99999, 2):
    if i % 2 == 0:
        if int(str(i)[2]) % 2 != 0:
            if sum(list(int(digit) for digit in str(i))) % 4 == 0:
                print(i)
