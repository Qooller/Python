# Давным-давно билет на одну поездку в метро стоил 15 рублей, билет на 10 поездок
# стоил 125 рублей, билет на 60 поездок стоил 440 рублей. Пассажир планирует
# совершить n поездок. Определите, сколько билетов каждого вида он должен приобрести,
# чтобы суммарное количество оплаченных поездок было не меньше n, а общая стоимость
# приобретенных билетов — минимальна.

n = int(input())
tr = {1: 15, 10: 125, 60: 440}
h = n
d = [0, 0, 0]

def do60(m):
    for i in range(m):
        d[0] = d[0] + 1
        while i % 10 == 8:
            d[0] = 0
            d[1] = d[1] + 1
            break
        while i % 10 == 9:
            d[0] = 0
            break
        while i == 34:
            d[0] = 0
            d[1] = 0
            d[2] = d[2] + 1
            break
        while 35 <= i <= 60:
            d[0] = 0
            d[1] = 0
            break
    print(d[0], d[1], d[2])


if n > 60:
    d[2] = n // 60
    n = n % 60
do60(n)

c1, c2, c3 = 15, 125, 440
N1, N2, N3 = 1, 10, 60


def cout(n1, n2, n3):
    return c1 * n1 + c2 * n2 + c3 * n3


def num_rides(n1, n2, n3):
    return N1 * n1 + N2 * n2 + N3 * n3


n1, n2, n3 = 0, 0, h//60
min_cost = 10**100
args = (0, 0, 0)
h %= 60
for num1 in range(9):
    for num2 in range(4):
        for num3 in range(2):
            if (num_rides(num1, num2, num3) >= h) and (cout(num1, num2, num3) < min_cost):
                min_cost = cout(num1, num2, num3)
                args = (num1, num2, num3)
print(args[0], args[1], args[2] + n3)
