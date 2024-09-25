from turtle import Turtle, Screen
from random import randint

race_on = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='TURTLE RACE!',
                       prompt="Enter a color to bet on: ")
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
y_positions = [-62.5, -37.5, -12.5, 12.5, 37.5, 62.5]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've won! The {winner} is the winner!")
            else:
                print(f"You've lost! The {winner} is the winner!")
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

    # purple = Turtle(shape='turtle')
    # blue = Turtle(shape='turtle')
    # green = Turtle(shape='turtle')
    # yellow = Turtle(shape='turtle')
    # orange = Turtle(shape='turtle')
    # red = Turtle(shape='turtle')

    # purple.penup()
    # purple.color('purple')
    # purple.goto(x=-230, y=-100)

    # blue.penup()
    # blue.color('blue')
    # blue.goto(x=-230, y=-75)

    # green.penup()
    # green.color('green')
    # green.goto(x=-230, y=-50)

    # yellow.penup()
    # yellow.color('yellow')
    # yellow.goto(x=-230, y=-25)

    # orange.penup()
    # orange.color('orange')
    # orange.goto(x=-230, y=0)

    # red.penup()
    # red.color('red')
    # red.goto(x=-230, y=25)


screen.exitonclick()
