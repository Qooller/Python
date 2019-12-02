#  Написать ф-ию factorial, которая принимает число,
#  а возвращает его факториал
import time
def factorial(a):
    b = 1
    i = 1
    while i != a+1:
        b = b * i
        i += 1
    return b
re = factorial(10)
print(re)

#Написать декоратор timeit, которые с помощью метода
#time библиотеки time  будет выводить
#вам время исполнения​ ф-ии по её завершению


def timeit(fn):
    def ttt(a):
        start = time.time()
        print('Start my function')
        fn(a)
        print('End my function')
        print(time.time()- start)
    return ttt
#@timeit
#def factorial():
#    print('Porcess')
factorial = timeit(factorial)

factorial(1000)
