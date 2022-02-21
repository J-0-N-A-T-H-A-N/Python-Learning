from turtle import Turtle

paddles = []


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(self.pos)
        self.shapesize(stretch_len=1, stretch_wid=5)
        paddles.append(self)

    def move_up_r(self):
        right = paddles[0]
        if right.ycor() >= 240:
            right.goto(right.xcor(), right.ycor())
        else:
            right.goto(right.xcor(), right.ycor() + 20)

    def move_down_r(self):
        right = paddles[0]
        if right.ycor() <= -240:
            right.goto(right.xcor(), right.ycor())
        else:
            right.goto(right.xcor(), right.ycor() - 20)

    def move_up_l(self):
        left = paddles[1]
        if left.ycor() >= 240:
            left.goto(left.xcor(), left.ycor())
        else:
            left.goto(left.xcor(), left.ycor() + 20)

    def move_down_l(self):
        left = paddles[1]
        if left.ycor() <= -240:
            left.goto(left.xcor(), left.ycor())
        else:
            left.goto(left.xcor(), left.ycor() - 20)
