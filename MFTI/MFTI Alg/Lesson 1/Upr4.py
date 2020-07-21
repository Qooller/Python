# # http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Упражнение №4: окружность
# Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный многоугольник
# с большим числом сторон будет выглядеть как окружность.

import turtle

turtle.shape('turtle')
for i in range(360):
    turtle.forward(1)
    turtle.left(1)
