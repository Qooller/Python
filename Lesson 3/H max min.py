# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a =[int(i) for i in input().split(' ')]
# i1 = i2 = 0
# b = []
# for j in range(len(a)):
#    if a[j] <= min(a):
#        i1 = j
#    elif a[j] >= max(a):
#        i2 = j
#    b.append(str(a[j]))
# b[i1], b[i2] = b[i2], b[i1]
# print(" ".join(map(str, b)))

i_max, i_min = a.index(max(a)), a.index(min(a))
a[i_max], a[i_min] = a[i_min], a[i_max]
print(*a)
