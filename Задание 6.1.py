# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]),
# а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
from itertools import chain, combinations, starmap, filterfalse, dropwhile
import sys

sp = list(chain([1, 2, 3], [4, 5], [6, 7]))
print(sp)

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code'])
# и возвращать массив из элементов, у которых длина не меньше пяти (['hello', 'world'])

v = list(filter(lambda x: len(x) > 4, ['hello', 'i', 'write', 'cool', 'code']))
print(v)


# Пример интересного итератора

def func(*args):
    if len(args) > 4:
        return args


data = list(dropwhile(func, ['hello', 'i', 'write', 'cool', 'code']))
print(data)

#как кодом на Python вывести на экран текущую версию Python
print(sys.version)

#как узнать время создания файла и его размер
import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime('D:\python')))
print("created: %s" % time.ctime(os.path.getctime('D:\python')))
print("size: %s" % (os.path.getsize('D:\python\\1.py')))

#Как убедиться, что по указанному пути существует директория (папка) и как вынести на экран список её содержимого
print("size: %s" % (os.path.isdir('D:\python')))
print("size: %s" % (os.path.exists('D:\python')))
print("size: %s" % (os.listdir('D:\python')))







