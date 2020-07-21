# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №7: спираль
# Нарисуйте спираль. См. теорию:
# https://ru.wikipedia.org/wiki/%D0%90%D1%80%D1%85%D0%B8%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0_%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BB%D1%8C

import turtle

turtle.shape('turtle')
for i in range(720):
        turtle.forward(1*i/360)
        turtle.left(2)
