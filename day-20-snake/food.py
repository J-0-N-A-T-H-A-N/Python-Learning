from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(60, 60)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x_pos = random.randint(-270, 270)
        rand_y_pos = random.randint(-270, 270)
        self.goto(rand_x_pos, rand_y_pos)