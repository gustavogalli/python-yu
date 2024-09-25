from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'
FONT_SIZE = 18
FONT_TYPE = 'normal'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score = self.score + 1
        self.write('')
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
