# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось.
# [4, 5, 8, 4, 7, 5, 9, 6, 2, 5, 7, 4, 5, 5, 9, 2, 6, 7, 4, 6, 5, 5, 0, 5, 2, 2, 6, 6,
#  8, 5, 6, 9, 4, 5, 6, 9, 8, 7, 4, 5, 3, 2, 1, 4, 5, 6, 8, 5, 2, 5, 6, 2, 4, 1, 5, 6]
a = [str(i) for i in input().split(' ')]
#b = []
#for i in a:
#    b.append(i)
#    if b.count(i) == 1:
#        print('NO')
#    else:
#        print('YES')

s = set()
for i in a:
    if i in s:
        print('YES')
    else:
        s.add(i)
        print('NO')
