# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
list = []
res_list = []
n_min = int(input("Введите начало диапазона: "))
n_max = int(input("Введите конец диапазона: "))
for i in range (0, int(input("Введите количество элементов: "))-1):
    list.append(randint(0, 50))
    if n_min <= list[i] <= n_max + 1:
        res_list.append(i)
print(list)
print(res_list)
