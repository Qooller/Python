import graphics as gr

window = gr.GraphWin("Dom", 800, 600)

# Фон
def sky_earth():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 300))
    earth = gr.Rectangle(gr.Point(0, 300), gr.Point(800, 600))

    sky.setFill('blue')
    earth.setFill('light gray')

    sky.draw(window)
    earth.draw(window)

# Солнце
def sun():
    sunn = gr.Circle(gr.Point(650, 80), 50)
    sunn.setFill('yellow')
    sunn.draw(window)

# дом
def house():
    house1 = gr.Rectangle(gr.Point(200, 200), gr.Point(400, 400))
    house1.setWidth(3)
    house1.setFill('gray')

    ruff = gr.Polygon(gr.Point(200, 200), gr.Point(300, 100), gr.Point(400, 200))
    ruff.setWidth(3)
    ruff.setFill('brown')
    wind = gr.Rectangle(gr.Point(250, 250), gr.Point(350, 350))
    wind.setWidth(3)
    wind.setFill('yellow')
    wind1 = gr.Line(gr.Point(300, 250), gr.Point(300, 350))
    wind2 = gr.Line(gr.Point(250, 300), gr.Point(350, 300))
    wind1.setWidth(3)
    wind2.setWidth(3)
    house1.draw(window)
    ruff.draw(window)
    wind.draw(window)
    wind1.draw(window)
    wind2.draw(window)

# Облоко
def cloud():
    cloud1 = gr.Circle(gr.Point(80, 60), 20)
    cloud2 = gr.Circle(gr.Point(95, 60), 20)
    cloud3 = gr.Circle(gr.Point(110, 75), 20)
    cloud4 = gr.Circle(gr.Point(90, 75), 20)
    cloud5 = gr.Circle(gr.Point(70, 75), 20)
    cloud1.setFill('white')
    cloud2.setFill('white')
    cloud3.setFill('white')
    cloud4.setFill('white')
    cloud5.setFill('white')
    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)

# елка
def tree():
    fir_tree1 = gr.Rectangle(gr.Point(590, 450), gr.Point(600, 500))
    fir_tree1.setWidth(3)
    fir_tree1.setFill('brown')
    fir_tree1.draw(window)
    for i in range(4):
        fir_tree2 = gr.Polygon(gr.Point(595, 400 - 40 * i), gr.Point(670, 450 - 40 * i), gr.Point(520, 450 - 40 * i))
        fir_tree2.setWidth(3)
        fir_tree2.setFill('green')
        fir_tree2.draw(window)


def paint():
    sky_earth()
    sun()
    house()
    cloud()
    tree()

paint()
#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()

window.close()