from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

POSITION = (350, 0)
SPEED = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle(2)
ball = Ball()
score = ScoreBoard()

# making the screen responsive (thus keyboard input)
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while True:
    while game_is_on:

        ball.move_ball()
        sleep(SPEED)
        screen.update()
        # detecting collision with y cor
        if abs(ball.ycor()) > 280:
            ball.setheading(-ball.heading())
        # detecting collision with paddle
        if ball.distance(l_paddle.pos()) <= 30 or ball.distance(r_paddle.pos()) <= 30:
            ball.bounce()

        # when ball goes on saved
        if ball.xcor() > 400:
            score.l_score += 1
            score.score()
            game_is_on = False
            sleep(SPEED)
        elif ball.xcor() < -400:
            score.r_score += 1
            score.score()
            game_is_on = False
            sleep(SPEED)
    ball.reset_()
    l_paddle.reset_()
    r_paddle.reset_()
    game_is_on = True
    sleep(SPEED)

# screen.exitonclick()
