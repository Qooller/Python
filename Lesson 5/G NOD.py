


a = 64 # int(input())
b = 96 # int(input())

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)
