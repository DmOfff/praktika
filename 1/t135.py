# Выведите случайную серию чисел из 0 и 1 такую, что сумма чисел в ней больше 10.

import random

x = [['1'] * random.randint(10, 50)][0] + [['0'] * random.randint(0, 50)][0]
random.shuffle(x)
print(''.join(x))
