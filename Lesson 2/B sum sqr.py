# По данному n вычеслить сумму 1^2+2^2+3^2+..+n^2.
n = int(input())
k = 0
for i in range(n+1):
    k = i * i + k

print(k)
