import graphics as gr

SIZE_X = 800
SIZE_Y = 600
x = 2.5
y = 1.7

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = gr.Point(200, 200)
# Ускорение
acceleration = gr.Point(0, 0)


# Фон
rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('green')
rectangle.draw(window)

thread1 = gr.Line(gr.Point(400, 0), gr.Point(200, 200))
thread1.setFill('red')
thread1.draw(window)
thread2 = gr.Line(gr.Point(400, 0), gr.Point(600, 200))
thread2.setFill('red')
thread2.draw(window)
thread3 = gr.Line(gr.Point(400, 0), gr.Point(400, 270))
thread3.setFill('red')
thread3.draw(window)

# Шарик
circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

def add(point_1, point_2x, point_2y):
    new_point = gr.Point(point_1.x + point_2x,
                         point_1.y + point_2y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point

def update_coords(coords, x1, y1):
    return add(coords, x1, y1)

def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)


while True:
    acceleration = update_acceleration(coords, gr.Point(400, 0))
    x += acceleration.x
    y += acceleration.y
    circle.move(x, y)
    coords = update_coords(coords, x, y)
    if coords.x - 10 < 190 or coords.x + 10 > 601:
        x = -x
        y = -y


    gr.time.sleep(0.02)

#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()
window.close()