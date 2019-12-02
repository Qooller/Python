# Даны три натуральных числа a, b, c. Определите, существует ли треугольник
# с такими сторонами. Если треугольник существует, выведите строку YES,
#  иначе выведите строку NO. Треугольник — это три точки, не лежащие на одной прямой.
m = 0
a, b, c = int(input()), int(input()), int(input())
if a >= b:
    if a >= c:
        print("YES" if a < (c + b) else "NO")
    else:
        print("YES" if c < (a + b) else "NO")
elif b >= c:
    print("YES" if b < (a + c) else "NO")
else:
    print("YES" if c < (a + b) else "NO")

# Либо так:
# a, b, c = [int(i) for i in input().split(',')}
# d = max(a,b,c)
# print("YES" if a + b + c > 2 * d else "NO")


