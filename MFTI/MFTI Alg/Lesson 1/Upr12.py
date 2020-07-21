# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №12: пружина
# Нарисуйте пружину. Используйте функцию, рисующую дугу.

n = 3
import turtle

turtle.shape('turtle')
turtle.left(90)


def spr():
    for i in range(90):
        turtle.forward(1)
        turtle.right(2)
    for j in range(90):
        turtle.forward(0.1)
        turtle.right(2)
for k in range(n):
    spr()