from turtle import Turtle

class GameChar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.step = 20

    def move_up(self):
        if self.ycor() >= 280:
            self.goto(self.xcor(), self.ycor())
        else:
            self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        if self.ycor() <= -280:
            self.goto(self.xcor(), self.ycor())
        else:
            self.goto(self.xcor(), self.ycor() - self.step)

    def reset(self):
        self.goto(0, -280)
