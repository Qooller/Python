# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №6: паук
# Нарисуйте паука с n лапами

import turtle

n = 13
turtle.shape('turtle')
for i in range(n):
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180+360/n)



