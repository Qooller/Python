# Напишите класс "Координата". При создании объекта
# должны приниматься значение оси X и значение оси Y.
# Класс должен иметь метод, который возращает число от 1 до 4,
# тем самым показывая, в каком участке находится точка.
class Koor:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sektor(self):
        if self.x > 0:
            if self.y > 0:
                return 'Координаты лежат в секторе 1'
            elif self.y < 0:
                return 'Координаты лежат в секторе 4'
        elif self.x < 0:
            if self.y > 0:
                return 'Координаты лежат в секторе 2'
            elif self.y < 0:
                return 'Координаты лежат в секторе 3'
    def dlina(self):
        return (self.x ** 2 + self.y ** 2)**(1/2)

k1 = Koor(-3,4)
obl = k1.sektor()
d = k1.dlina()
print(obl)
print('Длина равна {0:.2f}'.format(d))


