# Выведите  на экран строки (в последней строке n звездочек):
# *
# **
# ***
# ****
# *****


n = int(input("Укажите количество строк: "))
z = "*"
for i in range(1, n + 1):
    print(z * i)
