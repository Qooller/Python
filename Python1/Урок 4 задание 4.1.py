#Класс Деньги для работы с денежными суммами.
#Один объект должен быть иметь два аттрибута: рубли и копейки.
#Объект должен иметь метод, возращающий эквивалент объекта
#только в копейках в виде целого числа.
#На экран объект должен выводится как "x руб. y коп."
#(есть специальный магический метод, отвечающий за то,
#как объект выводится на экран).
#Реализовать сложение, вычитание и операции сравнения
#между объектами деньгами (для этого есть специальные магические методы).

class Money:
    rub = 0
    kop = 0
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop
    def vozvrat_kop(self):
        return self.rub*100 + self.kop
    def __repr__(self):
        return '{} руб.'.format(self.rub) + '{} коп.'.format(self.kop)
    def __add__(self, other):
        return '{} руб.'.format((self.vozvrat_kop() + other.vozvrat_kop()) // 100)\
               + '{} коп.'.format((self.vozvrat_kop() + other.vozvrat_kop()) % 100)
    def __sub__(self, other):
        return '{} руб.'.format((self.vozvrat_kop() - other.vozvrat_kop()) // 100)\
               + '{} коп.'.format((self.vozvrat_kop() - other.vozvrat_kop()) % 100)
    def __gt__(self, other):
        return self.vozvrat_kop() > other.vozvrat_kop()
    def __lt__(self, other):
        return self.vozvrat_kop() < other.vozvrat_kop()
    def __eq__(self, other):
        return self.vozvrat_kop() == other.vozvrat_kop()


m1 = Money(3, 30) # создаем объект равным 3 рублям и 30 копейкам

penny = m1.vozvrat_kop()

print('m1 в копейках равен {}'.format(penny))
# "m1 в копейках равен 330'

print(type(m1))
# int

m2 = Money(4, 95)

m3 = m1 + m2
print(type(m3))

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."
if m1 == m2:
    print('{} и {} равны'.format(m1, m2))
elif m1 > m2:
    print('{} больше чем {}'.format(m1, m2))
else:
    print('{} меньше чем {}'.format(m1, m2))

