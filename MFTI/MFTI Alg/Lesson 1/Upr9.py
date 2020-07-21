# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №9: правильные многоугольники
# Нарисуйте 10 вложенных правильных многоугольников.
# Используйте функцию, рисующую правильный n-угольник. Формулы для нахождения радиуса описанной окружности.

import turtle
turtle.shape('turtle')
def mgr(n,a):
    turtle.left(60 + 360 / n)
    for i in range(n):
        turtle.forward(5*n+30)
        turtle.left(360 / n)
    turtle.penup()
    turtle.right(60+360 / n)
    turtle.forward(10)
    turtle.pendown()
for j in range(3,13,1):
    mgr(j,20)
