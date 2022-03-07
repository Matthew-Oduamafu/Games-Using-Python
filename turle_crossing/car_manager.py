from turtle import Turtle
from random import choice, randint
from player import MOVE_DISTANCE
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super(CarManager, self).__init__("square")
        self.create_car()

    def create_car(self):
        pos = (randint(-280, 280), randint(-280, 280))
        self.penup()
        self.speed("fastest")
        self.goto(pos)
        self.color(choice(COLORS))
        self.turtlesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        super(CarManager, self).reset()
        self.create_car()
        pos = (280, randint(-280, 280))
        self.goto(pos)


# alternative solution
class CarManager1:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        dice = randint(1, 6)
        if dice == 1:
            car = Turtle("square")
            pos = (300, randint(-280, 280))
            car.penup()
            car.speed("fastest")
            car.goto(pos)
            car.color(choice(COLORS))
            car.turtlesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            self.all_cars.append(car)

    def move(self):
        [car.forward(MOVE_DISTANCE) for car in self.all_cars]

    def drop_car(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                car.clear()

    def reset(self):
        for car in self.all_cars:
            car.clear()
        self.all_cars = []
