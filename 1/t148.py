# Пользователь вводит положительное целое число.
# Зашифровать каждую цифру серией из букв (конкретный принцип составления серии букв разработать самостоятельно).

keys = {
    '0': 'ab',
    '1': 'bv',
    '2': 'sg',
    '3': 'gb',
    '4': 'ey',
    '5': 'vc',
    '6': 'qh',
    '7': 'su',
    '8': 'vn',
    '9': 'ja',
}


def crypt(x):
    return keys[x]


def decrypt(x):
    for num, value in keys.items():
        if value == x:
            return str(num)


x = int(input())

crypted = ''

for i in str(x):
    crypted += crypt(i)

print(str(x) + " зашифрован в: " + str(crypted))

encrypted = ''
i = 2
while i <= len(crypted):
    encrypted += decrypt(crypted[slice(i-2, i)])
    i += 2

print(str(crypted) + " зашифрован в: " + str(encrypted))