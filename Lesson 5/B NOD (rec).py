# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель.
# Примечание. В программе запрещается использовать циклы.
# Входные данные
# Вводятся два натуральных числа A и B (A, B ≤ 109).
# Выходные данные
# Требуется вывести НОД A и B.

a, b = [int(i) for i in input().split(' ')]
def nod(a, b):
    if a == 0 :
        return b
    elif b == 0:
        return a
    elif a > b:
        return nod(a % b, b)
    else:
        return nod(a, b % a)


print(nod(a, b))
