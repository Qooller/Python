# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №11: «бабочка»
# Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.

n = 5
import turtle

turtle.shape('turtle')
turtle.left(90)


def flower(m):
    for i in range(180):
        turtle.forward(2+m)
        turtle.left(2)
    for j in range(180):
        turtle.forward(2+m)
        turtle.right(2)

for k in range(n):
    flower(k)

