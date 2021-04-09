# Пользователь вводит четыре числа.
# Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"

nums = []
for i in range(4):
    n = int(input(""))
    if n % 2 == 0:
        nums.append(n)

print(max(nums) if len(nums) > 0 else "not found")

