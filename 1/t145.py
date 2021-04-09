# Пользователь вводит англ. букву, вывести следующие три по алфавиту.
# Если алфавит закончился, то вывести циклично с начала алфавита, то есть если z, то a b c.
# Вывод только маленьких букв. Учесть, что пользователь может ввести заглавную

import string

s = input().lower()

if len(s) > 1:
    print("Нужно ввести только 1 букву!")
    quit()

index = string.ascii_lowercase.index(s)

alphabet = string.ascii_lowercase + string.ascii_lowercase

print(alphabet[index + 1])
print(alphabet[index + 2])
print(alphabet[index + 3])
