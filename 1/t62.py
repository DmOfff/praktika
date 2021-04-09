# Дано пятизначное число. Цифры на четных позициях занулить. Например, из 12345 получается число 10305.

n = list(input())

for index, i in enumerate(n):
    if (index-1) % 2 == 0:
        n[index] = '0'

print("".join(n))
