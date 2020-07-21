# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №13: смайлик
# Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.
import turtle


def spr(n, r, clr):
    turtle.begin_fill()
    for i in range(90*n):
        turtle.forward(r)
        turtle.right(2)
    turtle.color(clr)
    turtle.end_fill()


turtle.shape('turtle')
turtle.left(90)
spr(2, 3, "yellow")
turtle.color("black")
turtle.penup()
turtle.goto(20,25)
turtle.pendown()
spr(2, 0.5, "blue")
turtle.color("black")
turtle.penup()
turtle.goto(120,25)
turtle.pendown()
spr(2, 0.5, "blue")
turtle.color("black")
turtle.penup()
turtle.goto(80,15)
turtle.left(180)
turtle.pendown()
turtle.width(10)
turtle.forward(30)

turtle.penup()
turtle.forward(20)
turtle.goto(140,-25)
turtle.pendown()
turtle.color("red")
spr(1,1.8,"red")


