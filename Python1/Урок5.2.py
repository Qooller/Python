#Реализацию функции reversed: ф-ия принимает список,
# возращает его, но элементы расположенны в обратном порядке

def reversed1(s):
    z = []
    for i in range(len(s)):
        z.insert(-i, s[i])
#        i += 1
    return z
r = reversed1([3, 9, 7, 8, 6])
print(r)
