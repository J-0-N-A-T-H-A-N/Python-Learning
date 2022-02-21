from turtle import Turtle

STEP = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        if self.ycor() <= 275:
            self.forward(STEP)

    def move_down(self):
        if self.ycor() >= -275:
            self.backward(STEP)

    def reset_player(self):
        self.goto(STARTING_POSITION)
