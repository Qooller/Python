from graph import *


penSize(0)
brushColor(50, 200, 250)
rectangle(0, 0, 600, 300)
brushColor("blue")
rectangle(0, 300, 600, 450)
brushColor("yellow")
rectangle(0, 450, 600, 600)
brushColor("yellow")
circle(440, 100, 50)


brushColor("white")
penSize(1)
circle(150, 100, 15)
circle(135, 110, 15)
circle(170, 100, 15)
circle(155, 110, 15)
circle(175, 110, 15)
circle(190, 100, 15)
circle(200, 108, 15)
brushColor(250, 130, 90)

rectangle(220, 330, 370, 360)
polygon([(370,360), (370,330),
         (370,330), (450,330)])
brushColor("white")
circle(387, 342, 7)
penSize(8)
line(280, 330, 280, 210)
penSize(2)
polygon([(280,330), (300,270),
         (340,270), (280,330)])
polygon([(280,210), (300,270),
         (340,270), (280,210)])
penSize(1)
brushColor(250, 170, 90)
polygon([(120, 360), (30, 390), (210,390)])
brushColor(250, 170, 100)
penSize(0)
rectangle(115, 360, 125, 500)


run()