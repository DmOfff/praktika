# Дано четырехзначное число. Переставьте местами цифры так, чтобы сначала оказались цифры, меньшие пяти.

n = input()

if len(n) != 4:
    print("Число не 4х значное")
    quit()


def reorder(number, cutoff=5):
    digits = []
    while number > 0:
        number, mod = divmod(number, 10)
        digits.append(mod)
    digits.reverse()
    digits = [x for x in digits if x < cutoff] + [x for x in digits if x >= cutoff]
    result = 0
    while digits:
        result *= 10
        result += digits.pop(0)
    return result


print(reorder(int(n)))
