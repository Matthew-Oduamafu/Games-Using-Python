from turtle import Turtle

POSITION = [(-350, 0), (350, 0)]


class Paddle(Turtle):

    def __init__(self, player_number=1):
        """
        Creates a player paddle
        :param player_number: int, 1 or 2 default = 1
               the number determines which player
        """
        super().__init__()
        self.player_number = player_number
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        if self.player_number == 1:
            self.goto(POSITION[-1])
        elif self.player_number == 2:
            self.goto(POSITION[0])
        else:
            print("Player number must be 1 or 2")
            return None
        self.color("white")
        self.speed(1)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)

    def reset_(self):
        self.create_paddle()
