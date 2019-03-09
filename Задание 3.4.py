#Написать функцию is_prime, принимающую 1 аргумент —
#  число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
def is_prime(s):
    for i in range(2, s-1):
        if s % i == 0:
            return False
#    for j in range(2, s-1):
#        if s % j == 0:
 #           return False
    return True




g = is_prime(67)
print(g)




