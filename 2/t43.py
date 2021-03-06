# В строке записано десятичное число. Запишите данное число римскими цифрами.

def to_roman(data):
    base = "I" * data

    base = base.replace("I" * 5, "V")
    base = base.replace("V" * 2, "X")
    base = base.replace("X" * 5, "L")
    base = base.replace("L" * 2, "C")
    base = base.replace("C" * 5, "D")
    base = base.replace("D" * 2, "M")

    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")

    return base


n = int(input())

print(str(n) + " --> " + to_roman(n))
