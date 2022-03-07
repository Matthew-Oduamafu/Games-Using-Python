from turtle import Turtle
FONT = ("consolas", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-230, 250)
        self.write("Level {0}".format(self.score), align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
