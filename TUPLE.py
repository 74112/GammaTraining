import turtle

turtle.goto(-125, -125)
def move(a):
    turtle.forward(a)
    turtle.left(90)


def drawSquwer(a):
    for i in range(4):
        move(a)


def DrawSquwerColor(a, color):
    turtle.color(color)
    turtle.begin_fill()
    drawSquwer(a)
    turtle.end_fill()


turtle.speed(1)

DrawSquwerColor(100, "purple")

turtle.goto(125, 125)

DrawSquwerColor(200, "blue")

turtle.goto(0, 125)

DrawSquwerColor(150, "red")
