# Сгенерировать пароль для пользователя.
# Требования: длина от 6 до 20 символов,
# должен быть ровно один символ подчеркивания,
# хотя бы две заглавных буквы,
# не более 5 цифр, любые две цифры подряд недопустимы.

import random
import string

size = random.randint(6, 20)
password = []

for i in range(0, random.randint(1, 6)):
    password.append(random.randint(0, 9))

for i in range(0, 2):
    password.append(string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)].upper())

random.shuffle(password)

if len(password) >= size:
    print(''.join(str(x) for x in password))
else:
    for i in range(0, size - len(password)):
        s = string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)]
        if random.randint(0, 1) == 1:
            password.append(s.upper())
        else:
            password.append(s)

    random.shuffle(password)
    print(''.join(str(x) for x in password))