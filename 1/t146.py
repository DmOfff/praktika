# Вывести англ. алфавит по 5 букв в строке


for i in range(65, 91):
    if (i - 1) % 5 == 0:
        print()
    print(chr(i) + chr(i + 32) + ' ', end='')
