# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №5: больше квадратов
# Нарисуйте 10 вложенных квадратов.

import turtle

turtle.shape('turtle')
for i in range(10):
    turtle.forward(20+i*10)
    turtle.left(90)
    turtle.forward(20+i*10)
    turtle.left(90)
    turtle.forward(20+i*10)
    turtle.left(90)
    turtle.forward(20+i*10)
    turtle.penup()
#    turtle.forward(5)
#    turtle.right(90)
#    turtle.forward(5)
#    turtle.left(180)
    turtle.goto(-5-5*i, -5-5*i)
    turtle.left(90)
    turtle.pendown()
