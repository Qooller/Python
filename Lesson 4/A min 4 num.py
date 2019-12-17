# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if, а использует стандартную функцию min.
# Считайте четыре целых числа и выведите их минимум.

a, b, c, d = int(input()), int(input()), int(input()), int(input())

def min4(a, b, c, d):
    e = min(a, b)
    f = min(c, d)
    g = min(e, f)
    return g
print(min4(a,b,c,d))

