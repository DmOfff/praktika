# Дан текст. Найти сумму имеющихся в нем цифр.

s = input()
print(sum([int(x) for x in s if x.isdigit()]))
