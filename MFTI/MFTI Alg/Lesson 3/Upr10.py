# Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел
# (не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему
# элементу. Числа, следующие за числом 0, считывать не нужно.

i = 1
a = 0
d = []
while i != 0:
    i = int(input())
    if i == 0:
        break
    elif a <= i:
        a = i
        d.append(i)
print(d.count(a))