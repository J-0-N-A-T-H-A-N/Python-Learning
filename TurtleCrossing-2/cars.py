from turtle import Turtle
import random

CAR_MOVE = 10


class Car:
    def __init__(self):
        self.car_list = []
        self.car_speed = 0.15

    def create_car(self):
        if random.randint(1, 5) == 1:
            color_list = ["red", "blue", "green", "purple", "yellow", "orange", "brown"]
            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(color_list))
            y_pos = random.randrange(-230, 250, 30)
            car.goto(300, y_pos)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(CAR_MOVE)
