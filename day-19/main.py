from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
screen = Screen()
tim.setheading(90)


def forwards():
    tim.forward(10)


def backwards():
    tim.back(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.setheading(90)


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
