# 25th Feb, 2022
# Module to keep track of score in the Snake game
# Author: Matthew

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("consolas", 14, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.high_score = self.read_high_score()
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {0}\tHigh score: {1}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.high_score, self.score)
        self.score = -1
        self.increase_score()
        self.save_high_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        self.score = -1 # redundant
        with open("data.txt", "r") as file:
            saved_score = int(file.read())
        return saved_score

    def save_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
