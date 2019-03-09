#Написать ф-ию wave, которая будет принимать строку,
# а возвращать список строк с такими же символами,
# но один из символов будет заглавным

def wave(st):
    sp = []
    dl = len(st)
    for i in range(0, dl):
        h = st[:i] + st[i].upper() + st[i+1:]
        sp.append(h)
    return sp
w = wave('hello')
print(w)