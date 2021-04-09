# В данном массиве найдите количество чисел, соседи у которых отличаются более чем в 2 раза.

lis = [1, 2, 3, 4, 4, 6, 7, 12]

for index, i in enumerate(lis[1:-1]):
    if lis[index-1] * 2 > i and lis[index+1] * 2 > i:
        print(i)