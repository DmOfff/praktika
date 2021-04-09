# Даны три числа. Найдите те два из них, сумма которых наибольшая.

nums = list([int(input()), int(input()), int(input())])

del nums[nums.index(min(nums))]

for i in nums:
    print(i, end=' ')