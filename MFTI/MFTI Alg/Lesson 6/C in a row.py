# Вводится последовательность, состоящая только из 0 и 1. Необходимо найти максимальное количество 1,
# идущих подряд (без 0 между ними).
# Формат входных данных
# В первой строке задается натуральное N<=10000 , длина массива, далее идут N чисел 0 или 1 -- элементы массива.
# Каждое число вводится с новой строки.
# Формат выходных данных
# Одно число — результат.

b = []
l = []
k = 0
try:
    n = int(input())
    for i in range(n):
        b.append(int(input()))
except ValueError:
    l = []
else:
    for i in b:
        if i == 0:
            l = []
        elif i == 1:
            l.append(i)
            if k < len(l):
                k = len(l)
print(k)
