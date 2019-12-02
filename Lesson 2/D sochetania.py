# По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k, то есть n!/(k!*(n−k)!.

n, k = int(input()), int(input())
# r1, r2, r3 = 1, 1, 1
# for i in range(1, n+1):
#    r1 = i * r1
# for i in range(1, k+1):
#    r2 = i * r2
# for i in range(1, n-k+1):
#    r3 = i * r3
# print(int(r1/r2/r3))

def factorial(n):
    r1 = 1
    for i in range(1, n + 1):
        r1 = i * r1
    return r1
print(int(factorial(n)/factorial(k)/factorial(n-k)))
