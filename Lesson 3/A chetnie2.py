# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# Программа должна быть эффективной и не выполнять лишних действий!

a = [str(i) for i in input().split(' ')]
b = []
k = 0
for i in a:
    if k % 2 == 0:
        b.append(i)
    k += 1
print(' '.join(b))
# print(*a[::2], sep=" ")