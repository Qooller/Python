# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). Если элементов
# нечетное число, то последний элемент остается на своем месте.
a = [str(i) for i in input().split(sep=' ')]
if len(a) % 2 == 0:
    for j in range(0, len(a), 2):
        a[j], a[j+1] = a[j+1], a[j]
else:
    for j in range(0, len(a)-1, 2):
        a[j], a[j+1] = a[j+1], a[j]
print(' '.join(a))
print(*a)







