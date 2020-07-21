# # http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №10: «цветок»
# Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность.

n = 5
import turtle

turtle.shape('turtle')


def flower(n):
    for i in range(180):
        turtle.forward(1)
        turtle.left(2)
    for j in range(180):
        turtle.forward(1)
        turtle.right(2)
    turtle.left(180 / n)

for k in range(n):
    flower(n)