# Даны два натуральных числа N и K. Требуется вывести  все цепочки
# x1, x2, ..., xN такие, что xi - натуральное и 1 ≤ xi ≤ K.
# Входные данные
# Вводятся два натуральных числа N и K (N, K ≤ 6).
# Выходные данные
# Выведите все требуемые цепочки в произвольном порядке – по одной на строке. Никакая цепочка
# не должна встречаться более одного раза.

n, k = 2, 3 # [int(i) for i in input().split(' ')]
h = []

def sp(y):

    if y == 0:
        for it in range(n):
            h.append(1)
        return h
    else:
        return sp(y-1)
print(sp(3))
r = 0
mas = []
for i in range(pow(k, n)):
    mas.append([])
    for j in range(n):
        mas[i].append(j+1)
        r += 1
        print(mas[i][j], end=' ')
    print()
# print(mas)



