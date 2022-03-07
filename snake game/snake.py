# 25th Feb, 2022
# module for creating the snake object
# Author: Matthew

from turtle import Turtle

START_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
SNAKE_SIZE = (0.5, 0.5)


class Snake:
    segments = []

    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POSITION:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(pos)
            turtle.shapesize(*SNAKE_SIZE)
            self.segments.append(turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def grow(self):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.segments[-1].pos())
        turtle.shapesize(*SNAKE_SIZE)
        self.segments.append(turtle)

    def collision_with_tail(self):
        collided = False
        for seg in self.segments[2:]:
            if self.head.pos() == seg.pos():
                collided = True
                break
        return collided

    def reset(self):
        [seg.hideturtle() for seg in self.segments]
        # alternative way of removing the snakes from the screen
        # [seg.goto(1000, 1000) for seg in self.segments]
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

