# 25th Feb, 2022
# module controlling the food the snake picks
# Author: Matthew

from turtle import Turtle, colormode
from random import randint, choice
SHAPES = ["arrow", "turtle", "circle", "square", "triangle"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        colormode(255)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.default()

    def resize_food(self):
        self.turtlesize(1.2, 1.2)

    def default(self):
        self.shape(choice(SHAPES))
        self.turtlesize(0.8, 0.8)
        color = randint(10, 255), randint(0, 255), randint(0, 255)
        pos = randint(-280, 280), randint(-280, 280)
        self.color(color)
        self.goto(pos)
