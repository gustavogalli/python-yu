import turtle as t
import random


def random_color():
    t.colormode(255)
    r = random.randint(130, 255)
    g = random.randint(130, 255)
    b = random.randint(130, 255)
    random_color = (r, g, b)
    return random_color


def move(columns, rows):
    tim.goto(columns * -25, rows * -25)
    for _ in range(rows):
        for _ in range(columns):
            tim.dot(20, random_color())
            tim.forward(50)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50 * columns)
        tim.left(180)


tim = t.Turtle()
tim.hideturtle()
tim.up()
tim.speed(0)

move(10, 10)


screen = t.Screen()
screen.exitonclick()
