# Дано число. Если оно от 2 до 5 включительно, то увеличить его на 10. Если оно от 7 до 40,
# то уменьшить на 100. Если оно не более 0 или более 3000,
# то увеличить в 3 раза (то есть умножить на 3). Иначе занулить это число


a = int(input())
if 2 <= a <= 5:
    a += 10
elif 7 <= a <= 40:
    a -= 100
elif a <= 0 or a > 3000:
    a *= 3
else:
    a = 0
print(a)