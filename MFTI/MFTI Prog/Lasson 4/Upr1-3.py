
from graph import *
import time
print(windowSize())
windowSize(500, 600)
print(windowSize())


penSize(0)
brushColor(50, 200, 250)
rectangle(0, 0, 600, 300)
brushColor("blue")
rectangle(0, 300, 600, 450)
circle(350, 470, 40)
# Волны
brushColor("yellow")
rectangle(0, 450, 600, 600)
circle(85, 480, 40)
circle(195, 480, 40)
circle(305, 480, 40)
circle(415, 480, 40)
circle(525, 480, 40)

brushColor("blue")
circle(30, 420, 40)
circle(140, 420, 40)
circle(250, 420, 40)
circle(360, 420, 40)
circle(470, 420, 40)

brushColor("yellow")
circle(440, 100, 50)


# Облоко 1
brushColor("white")
penSize(1)
circle(220, 50, 15)
circle(205, 60, 15)
circle(240, 50, 15)
circle(225, 60, 15)
circle(245, 60, 15)
circle(260, 50, 15)
circle(270, 58, 15)

# Облоко 2
circle(350, 170, 10)
circle(340, 180, 10)
circle(365, 170, 10)
circle(355, 180, 10)
circle(370, 180, 10)
circle(380, 170, 10)
circle(387, 178, 10)

# Облоко 3
circle(80, 150, 20)
circle(50, 170, 20)
circle(110, 150, 20)
circle(80, 170, 20)
circle(110, 170, 20)
circle(135, 150, 20)
circle(147, 163, 20)


# карабль 1
def ship(x1, y1, x2, y2):
    for i in range(10):
        brushColor(250, 130, 90)
        rectangle(x1 + i, y1, x2 + i, y2)
        polygon([(x2 + i,y2), (x2 + i,y1), (450 + i,y1)])
        brushColor("white")
        circle(387 + i, 342, 7)
        penSize(8)
        line(300 + i, y1, 300 + i, 210)
        penSize(2)
        polygon([(300 + i,y1), (320 + i,270), (360 + i,270)])
        polygon([(300 + i,210), (320 + i,270), (360 + i,270)])
        time.sleep(1)
ship(220, 330, 370, 360)

# карабль 2
penSize(1)
brushColor(250, 130, 90)
rectangle(100, 315, 180, 330)
polygon([(180, 330), (180, 315), (220, 315)])
brushColor("white")
circle(190, 320, 3)
penSize(5)
line(140, 315, 140, 255)
penSize(2)
polygon([(140, 315), (150, 285), (170, 285)])
polygon([(140, 255), (150, 285), (170, 285)])

# зонтик 1
penSize(1)
brushColor(250, 170, 90)
polygon([(120, 360), (30, 390), (210,390)])
brushColor(250, 170, 100)
penSize(0)
rectangle(115, 360, 125, 550)

# зонтик 2
penSize(1)
brushColor(250, 170, 90)
polygon([(340, 400), (295, 420), (385,420)])
brushColor(250, 170, 100)
penSize(0)
rectangle(337, 400, 343, 480)

run()