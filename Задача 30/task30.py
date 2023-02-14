# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый член последовательности: "))
n = int(input("Введите количество членов последовательности: "))
d = int(input("Введите d: "))

# def new_item(a, n, d):
#     return a + (n-1) * d
#
# list = [a1]
# for i in range(2, n):
#     list.append(new_item(a1, i, d))
list = []
def new_item(a, n, d, count):

    if count == 1:
        return a + (n - 1)*d
    list.append(a + (n - count)*d)
    return new_item(a, n, d, count - 1)

list.append(new_item(a1, n, d, n))
print(list)