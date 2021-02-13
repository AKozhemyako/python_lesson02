# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

a = 2
b = 1
c = 3
d = 3

min_local = find_min(find_min(a,b),find_min(c,d))

print(min_local)