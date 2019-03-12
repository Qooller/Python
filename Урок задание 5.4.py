#Реализацию range: Функция range() может принимать от одного до трех агрументов,
# при этом аргументами должны быть целые числа (int). range(старт, стоп, шаг) -
#  так выглядит стандартный вызов функции range() в Python. По умолчанию старт
# равняется нулю, шаг единице. Возвращает список целых чисел в форме
# [старт, старт + шаг, старт + шаг*2...]. Если шаг положительное число, последним
#  элементом списка будет наибольшее старт + i * шаг меньшее числа стоп. Если шаг
#  отрицательное число, то последний элемент будет наименьшее старт + i * шаг большее числа стоп.

def my_range(start = 0, stop = 1, h = 1):
    sp = []
    i = 0
    if h > 0:
        while stop > (start + h * i):
            n = (start + h * i)
            sp.append(n)
            i += 1
    else:
        while stop < (start + h * i):
            n = (start + h * i)
            sp.append(n)
            i += 1
    return sp
p = my_range(2,60,10)
print(p)
rrr = []
for j in range(2, 60, 10):
    rrr.append(j)
print(rrr)