# По данному целому неотрицательному n вычислите значение n!.
n = int(input())
k = 1
for i in range(1, n+1):
    k = i * k

print(k)

