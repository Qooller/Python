# Одно из типичных приложений для демонстрации очереди в действии - это симуляция реальной ситуации,
# которая требует управления данными в манере FIFO. Для начала давайте рассмотрим детскую игру Hot Potato.
# В этой игре (см. рисунок) дети выстраиваются в круг и перебрасывают предмет от соседа к соседу так быстро,
# как только могут. В некоторый момент игры действие останавливается, и ребёнок, у которого в руках остался
# предмет (картошка), выбывает из круга. Игра продолжается до тех пор, пока не останется единственный победитель.


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    print(simqueue.items)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    print(simqueue.items)
    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 15))