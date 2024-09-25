# from turtle import Turtle, Screen
# import turtle
import turtle as t
import random


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down()


def draw_polygons():
    for num in range(3, 10):
        tim.speed(0)
        tim.color(colors[num - 3])
        for _ in range(num):
            tim.forward(pace)
            tim.right(360 / num)


def random_color():
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed(0)
    tim.color(random_color())
    for _ in range(200):
        tim.forward(30)
        tim.setheading(random.choice(directions))
        tim.color(random_color())


colors = ['red', 'orange', 'green', 'purple', 'blue', 'pink', 'black']
pace = 50

tim = t.Turtle()
tim.shape('turtle')
tim.color('red')


def draw_circle():
    circles = 5
    for _ in range(circles):
        tim.color(random_color())
        tim.speed(0)
        tim.circle(50)
        tim.right(360 / circles)


# draw_circle()
random_walk()
# draw_polygons()
# draw_dashed_line()
# draw_square()


screen = t.Screen()
screen.exitonclick()
