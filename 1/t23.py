# Известно, что x кг конфет стоит a рублей. О
# пределите, сколько стоит y кг этих конфет,
# а также сколько кг конфет можно купить на k рублей.
# Все значения вводит пользователь.

x = int(input("Количество килограмм: "))
a = int(input("Стоимость килограмма конфет: "))

price = a / x

y = int(input('Введите массу конфет: '))
print(f"{y} кг стоит: {y * price}")

k = int(input("Количество рублей: "))
print(f"На {k} можно купить: {k / price} кг")