# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов,
# иначе дополнить строку символами 'o' до длины 12.


s = input()

if len(s) > 10:
    s = s[:6]
    print(s)
else:
    s += ('o' * (12 - len(s)))
    print(s)