# 25th Feb, 2022
# Creating snake game using turtle module
# Author: Matthew

from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import ScoreBoard
COLLISION_BOUNDARY = 290
SNAKE_SPEED = [x/100 for x in list(range(10, 0, -1))]
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
i = 0
speed = 0.1
while game_is_on:
    screen.update()
    sleep(speed)
    snake.move()

    # detecting collision
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        if score.score >= 0 and score.score % 5 == 0:
            if i < len(SNAKE_SPEED)-1:
                i += 1
                speed *= 0.9
            food.resize_food()
        snake.grow()

    # detect collision with wall and tail
    if abs(snake.head.xcor()) > COLLISION_BOUNDARY or abs(snake.head.ycor()) > COLLISION_BOUNDARY or \
            snake.collision_with_tail():
        speed = 0.1
        score.reset()
        snake.reset()


screen.mainloop()
