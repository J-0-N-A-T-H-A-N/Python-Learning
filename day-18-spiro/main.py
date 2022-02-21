import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(move_size):
    rand_color = random_color()
    tim.color(rand_color)
    tim.circle(100)
    tim.setheading(tim.heading() + move_size)


tim = t.Turtle()
tim.speed(0)
tim.pensize(2)
t.colormode(255)
circle_radius = 150

size_of_gap = 5
for _ in range(int(360 / size_of_gap)):
    draw_spirograph(size_of_gap)



screen = t.Screen()
screen.exitonclick()
