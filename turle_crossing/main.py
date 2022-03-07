from time import sleep
from turtle import Screen
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager
NUMBER_OF_CARS = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player instance
player = Player()
# keeping track of level (score)
score = Scoreboard()

# creating car instance
cars = [CarManager() for _ in range(0, NUMBER_OF_CARS)]

screen.listen()
screen.onkey(fun=player.move, key="Up")

car_speed = 0.1
game_is_on = True
while game_is_on:
    sleep(car_speed)
    screen.update()
    # cars moving
    [car.move() for car in cars]

    # cars collision with the left side
    [car.reset() for car in cars if car.xcor() < -300]

    for car in cars:
        if player.distance(car) <= 25:
            game_is_on = False
            score.game_over()
            break

    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        score.score += 1
        score.update_score()
        car_speed *= 0.9
screen.mainloop()
