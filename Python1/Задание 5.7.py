# Сount_symbol: считает сколько раз символ встречается в строке:
def count_symbol(st, t):
    dl = len(st)
    n = 0
    for i in range(0, dl):
        if st[i] == t:
            n += 1
    return n
w = count_symbol('hello rofgj Dnfys fkj skfk ksjbsk ss', 'r')
print('Элемент встречатся {} раз(а)'.format(w))