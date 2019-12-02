# Даны числа a и b. Решите в целых числах уравнение ax+b=0.
# Выведите все решения этого уравнения, если их число конечно, выведите слово NO,
# если решений нет, выведите слово INF, если решений бесконечно много.
a, b = int(input()), int(input())
if b == 0 and a == 0:
    print('INF')
elif a != 0 and b % a == 0:
    print(int(-b / a))
else:
    print('NO')
