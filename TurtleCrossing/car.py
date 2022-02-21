from turtle import Turtle
from random import randrange, choice

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        color_list = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.color(choice(color_list))
        self.penup()
        self.place_cars()
        self.carspeed = 0.15

    def place_cars(self):
        x_pos = randrange(-300, 300, 60)
        y_pos = randrange(-250, 250, 30)
        self.goto(x_pos, y_pos)

    def move_cars(self):
        self.goto(self.xcor() - 20, self.ycor())
        if self.xcor() <= -300:
            self.goto(300, self.ycor())
