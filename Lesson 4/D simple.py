# Дано натуральное число x > 1. Проверьте, является ли оно простым. Программа должна вывести слово YES,
# если число простое и NO, если число составное.
# Решение оформите в виде функции IsPrime(x), которая возвращает True для простых чисел и False для
# составных чисел. Решение должно иметь сложность O(sqrt(x)).
import math
x = int(input())

def IsPrime(x):
   d = 2
   while d * d <= x and x % d != 0:
       d += 1
   return d * d > x

if IsPrime(x) == True:
    print("YES")
elif IsPrime(x) == False:
    print("NO")
