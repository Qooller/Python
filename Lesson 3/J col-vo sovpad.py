# Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел содержится
# одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]

print(len(set(a).intersection(set((b)))))
