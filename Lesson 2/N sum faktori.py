# По данному n вычеслить  сумму 1!+2!+3!+..+n!. В решении этой задачи можно использовать только 1 цикл.
n = int(input())
k = 1
s = 0
for i in range(1, n+1):
    k = i * k
    s = k + s
print(s)