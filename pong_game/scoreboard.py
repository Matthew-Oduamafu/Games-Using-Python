from turtle import Turtle

FONT = ("consolas", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(50, 250)
        self.write(self.r_score, align="center", font=FONT)
