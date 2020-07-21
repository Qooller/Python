
from graph import *

print(windowSize())
windowSize(500, 600)
print(windowSize())

penSize(0)
brushColor(50, 200, 250)
rectangle(0, 0, 600, 300)
brushColor("blue")
rectangle(0, 300, 600, 450)
circle(350, 470, 40)
brushColor("yellow")
rectangle(0, 450, 600, 600)


# Волны
def wave(x, y, size):
    while x<600:
        brushColor("blue")
        circle(x, y, size)
        brushColor("yellow")
        circle(x + 55, y + 60, size)
        x += 110
wave(0,420,40)

# sun
brushColor("yellow")
circle(440, 100, 50)

# Облока
def cloud(x, y, size):
    brushColor("white")
    penSize(1)
    circle(x, y, size)
    circle(x - size, y+size, size)
    circle(x + 1.5*size, y, size)
    circle(x + 0.5*size, y+size, size)
    circle(x + 2*size, y+size, size)
    circle(x + 3*size, y, size)
    circle(x + 3.7*size, y + 0.5*size, size)

cloud(220, 50, 15)
cloud(350, 170, 10)
cloud(80, 150, 20)

# карабль
def ship(x1, y1, size):
    penSize(1)
    brushColor(250, 130, 90)
    rectangle(x1 , y1, x1+150*size, y1 + 30*size)
    polygon([(x1+150*size, y1 + 30*size), (x1+150*size, y1), (x1+230*size, y1)])
    brushColor("white")
    circle(x1 + 167*size, y1 + 12*size, 6*size)
    penSize(8)
    line(x1 + 80*size, y1, x1 + 80*size, y1 - 120*size)
    penSize(2)
    polygon([(x1 + 80*size, y1), (x1 + 100*size, y1 - 60*size), (x1 + 140*size, y1 - 60*size)])
    polygon([(x1 + 80*size, y1 - 120*size), (x1 + 100*size, y1 - 60*size), (x1 + 140*size, y1 - 60*size)])
ship(220, 330, 1)
ship(100, 315, 0.5)

# зонтики
def umbrella(x, y, size):
    penSize(1)
    brushColor(250, 170, 90)
    polygon([(x, y), (x - 90*size, y + 30*size), (x + 90*size, y + 30*size)])
    brushColor(250, 170, 100)
    penSize(0)
    rectangle(x - 5*size, y, x + 5*size, y + 190*size)
umbrella(120, 360, 1)
umbrella(340, 400, 0.5)

run()


