# Сформировать убывающий массив из чисел, которые делятся на 3.

nums = []
for i in range(1, 1000):
    if i % 3 == 0:
        nums.append(i)

nums.reverse()

print(nums)