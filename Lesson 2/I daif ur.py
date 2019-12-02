# Даны числа a, b, c, d. Выведите в порядке возрастания все целые числа от 0 до 1000,
# которые являются корнями уравнения ax3+bx2+cx+d=0.
a, b, c, d = int(input()), int(input()), int(input()), int(input()) #[int(i) for i in input().split(',')]
for x in range(1001):
    if a*x**3+b*x**2+c*x+d == 0:
        print(x)
