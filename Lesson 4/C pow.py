# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите a^n не используя циклы и стандартную функцию pow, а используя рекуррентное соотношение a^n=a*a^(n−1).
# Решение оформите в виде функции power(a, n).

a, n = float(input()), float(input())


def power(a, n):
    if  n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * power(a, n-1)


print(power(a, n))
