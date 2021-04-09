# Реализуйте серию из n игр «Камень, ножницы, бумага» с компьютером.
# В результате выведите статистику: сколько игр выиграл пользователь,
# сколько раз каждого вида ходов было выбрано. Дополните игру анализом компьютера ваших ходов и
# выбор наиболее подходящего против вас хода.


import random


ver = 0
while ver == 0:
    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
    if player == 1 or player == 2 or player == 3:
        ver = 1
if player == 1:
    print("Вы выбрали камень.")
if player == 2:
    print("Вы выбрали ножницы.")
if player == 3:
    print("Вы выбрали бумагу.")
comp = random.randint(1, 3)
if comp == 1:
    print("Компьютер выбрал камень.")
if comp == 2:
    print("Компьютер выбрал ножницы.")
if comp == 3:
    print("Компьютер выбрал бумагу.")
if player == comp:
    win = 0
if player == 1 and comp == 2:
    win = 1
if player == 1 and comp == 3:
    win = 2
if player == 2 and comp == 1:
    win = 2
if player == 2 and comp == 3:
    win = 1
if player == 3 and comp == 1:
    win = 1
if player == 3 and comp == 2:
    win = 2
if win == 0:
    print("Ничья!")
if win == 1:
    print("Вы победили!")
if win == 2:
    print("Победил компьютер!")
