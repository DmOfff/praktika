# Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно.

s = list(input())
ss = []
for index, s in enumerate(s):
    if s == 'a' or s == 'b':
        ss.append(s.upper())
        continue
    ss.append(s)

print(''.join(ss))