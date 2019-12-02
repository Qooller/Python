#print(set({1,2,3} & {2,3,4,}))
#f = open('f.txt', 'wb')
#f.write(b'hjfk')
#f.close()
#f = open('f.txt','r')
#print(f.read())
#f.close()
#for line  in f:
#    \t
#    \\n
# r/ d:\ddd\jfh\text/txt  #raw - сырая строка

#a = [10, 27, 42, 36, 44, 353, 77]
#def maxa(x:int):
#    maxa = 0
#    for i in range(len(x)):
#        if a[i] > maxa:
#            maxa = a[i]
#        continue
#    return maxa
#print(maxa(a))

#class monitor:
#    pass
#m = monitor()
#m.on()


#class Employee:

 #   def __init__(self, first_name, last_name):
 #       self.first_name = first_name
 #       self.last_name = last_name
 #       self.login = (first_name[0] + last_name).lower()

# __init__ - конструктор класса, аналогично джаве и плюсам
#
#    def say(self, word):
#        print("{} say {}".format(self, word))


#e1 = Employee('Al', 'Rid')
#print(e1)

class Rectangle:
    def __init__(self, l, h):
        self.ll = l
        self.hh = h
    def per(self):
        return (self.ll + self.hh)*2
    def ss(self):
        return self.ll * self.hh
p = Rectangle(5,6)
print(p.ss())

class Square:
    def __init__(self, h):
       self.hh = h
    def per(self):
       return (self.hh) * 4
    def ss(self):
        return self.hh**2
sq = Square(5)
print(sq.ss())

class Square1(Rectangle):
   def __init__(self, h):
        self.hh = h
        self.ll = h
rr = Square1(7)
print(rr.per())




