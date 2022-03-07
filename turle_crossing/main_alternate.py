from time import sleep
from turtle import Screen
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player instance
player = Player()
# keeping track of level (score)
score = Scoreboard()

# creating car instance
cars = CarManager1()

screen.listen()
screen.onkey(fun=player.move, key="Up")

car_speed = 0.2
game_is_on = True
while game_is_on:
    sleep(car_speed)
    screen.update()
    # incoming cars
    cars.create_car()

    # moving the cars
    cars.move()

    # removing cars that has passed by
    cars.drop_car()

    for car in cars.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score.game_over()
            break

    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        score.score += 1
        score.update_score()
        car_speed *= 0.49
screen.mainloop()
