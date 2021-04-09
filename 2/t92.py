# Написать программу, реализующую процедуру удаления k символов с позиции номер n из строки S.

k = int(input('k: '))
n = int(input('n'))
s = input('s: ')

try:
    print(s[n:k])
except Exception:
    quit()