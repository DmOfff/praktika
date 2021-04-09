# Найдите количество целых чисел от a до b включительно, которые делятся на 12


a = int(input())
b = int(input())
count = 0
while a <= b:
    a = a + 1
    if a % 12 == 0:
        count = count + 1

print("Количество целых чисел, лежащих между a и b равно: ", count)
