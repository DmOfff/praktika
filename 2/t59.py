# Строка состоит из слов, разделенных одним или несколькими пробелами. Переставьте слова по убыванию их длин.

ss = input()

while "  " in ss:
    ss = ss.replace("  ", " ")

ss = ss.split(' ')

ss.sort(key=len)

print(' '.join(ss))