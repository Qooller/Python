# Посчитать количество четных элементов в массиве целых чисел, заканчивающихся нулём.
# Сам ноль учитывать не надо.

i = 1
summ = 0
while i != 0:
    i = int(input())
    if i == 0:
        break
    elif i % 2 == 0:
        summ += 1
print(summ)