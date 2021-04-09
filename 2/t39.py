# В данной строке вставить после каждого символа 'a' символ 'b'.

s = list(input())
ss = []
for index, s in enumerate(s):
    if s == 'a':
        ss.append(s)
        ss.append('b')
        continue
    ss.append(s)

print(''.join(ss))