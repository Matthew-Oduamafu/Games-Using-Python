from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.speed("fastest")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        super(Player, self).reset()
        self.create_turtle()
