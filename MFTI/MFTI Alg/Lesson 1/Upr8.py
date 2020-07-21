# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №8: квадратная «спираль»
# Нарисуйте «квадратную» спираль.

import turtle

turtle.shape('turtle')
for i in range(25):
    turtle.forward(10+5*i)
    turtle.left(90)

