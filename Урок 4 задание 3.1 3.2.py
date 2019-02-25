#  Написать ф-ию factorial, которая принимает число,
#  а возвращает его факториал
a = int(input('Введите целое число a: '))
def factorial():
    b = 1
    i = 1
    while i != a+1:
        b = b * i
        i += 1
    print(b)

#Написать декоратор timeit, которые с помощью метода
#time библиотеки time  будет выводить
#вам время исполнения​ ф-ии по её завершению

import time
def timeit(factorial):
    def ttt():
        time.clock()
        print('Start my function')
        factorial(1000)
        print('End my function')
        print(time.clock())
    return ttt

@timeit
def factorial():
    print('proc', a)


print(timeit(1000))