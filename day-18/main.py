import turtle
import turtle as t
import random

def random_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    random_color = (R, B, G)
    return random_color


tim = t.Turtle()
tim.shape("turtle")
tim.pensize(4)
tim.speed(3)
distance = 30
tim.penup()
tim.setposition(300, 300)
tim.pendown()
tim.setposition(300,-300)
tim.setposition(-300, -300)
tim.setposition(-300, 300)
tim.setposition(300, 300)
tim.penup()
tim.setposition(0,0)
tim.pendown()
tim.pensize(6)
direction = [0, 90, 180, 270]
t.colormode(255)

while -300 < tim.xcor() < 300 and -300 < tim.ycor() < 300:
    color = random_color()
    tim.color(color)
    angle = random.randint(0,360)
    if random.choice(direction) == 0:
        tim.forward(distance)
    elif random.choice(direction) == 90:
        tim.right(angle)
        tim.forward(distance)
    elif random.choice(direction) == 180:
        tim.back(distance)
    else:
        tim.left(angle)
        tim.forward(distance)

screen = t.Screen()
screen.exitonclick()
