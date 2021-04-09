# Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.

x = int(input('x: '))
d = int(input('d: '))
nums = []

for i in range(x, 1000, d):
    nums.append(i)

print(nums)