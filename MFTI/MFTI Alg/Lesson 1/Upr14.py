# # http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №14: звезды
# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.


import turtle

turtle.shape('turtle')



def star(n):
    for i in range(n):
        turtle.forward(70)
        turtle.left((n-(n-1)/2)*360/n)

star(5)
turtle.penup()
turtle.forward(120)
turtle.pendown()
star(11)