# По данным числам n и k (0<=k<=n) вычислите С(k,n). Для решения используйте рекуррентное соотношение
# C(n,k)=C(n−1,k−1)+C(k,n−1).
# Решение оформите в виде функции C(n, k).

n, k = int(input()), int(input())


def factorial(l):
    r1 = 1
    for i in range(1, l + 1):
        r1 = i * r1
    return r1


def C(n, k):
    c = int(factorial(n)/factorial(k)/factorial(n-k))
    if n == 0:
        return 1
    elif n == 1:
        return c
    else:
        return C(n-1, k-1) + C(n-1, k)


print(C(n, k))
