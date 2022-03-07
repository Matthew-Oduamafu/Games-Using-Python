from turtle import Turtle
from random import choice

POSITION = (0, 0)
HEADING_VALUE = choice((143.11, 36.89))  # 36.86989765


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.goto(POSITION)
        self.color("white")
        self.speed(50)
        self.showturtle()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(HEADING_VALUE)

    def move_ball(self):
        self.forward(20)

    def bounce(self):
        self.setheading(180 - self.heading())

    def reset_(self):
        self.create_ball()
