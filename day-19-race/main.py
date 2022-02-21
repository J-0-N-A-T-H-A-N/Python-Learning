from turtle import Turtle, Screen
import random

color_list=[
    "red",
    "blue",
    "purple",
    # "orange",
    # "pink",
    # "green",
    # "cyan",
    # "black"
]

is_race_on = False
screen=Screen()
screen.setup(width=1000, height=400)
screen.title("Welcome to the Races!")
color_string = ""
for color in color_list:
    if color == color_list[len(color_list) - 1]:
        color_string += "or " + color.capitalize()
    else:
        color_string += "{0}, ".format(color.capitalize())
string = "Who will win?\n" + color_string
bet = screen.textinput(f"Racetime!", string)
racer_list = []
random.shuffle(color_list)

starter = Turtle()
starter.speed("fastest")
starter.color("darkcyan")
starter.hideturtle()
starter.penup()
starter.setposition(-400, -82)
starter.pensize(3)
starter.setheading(90)
starter.pendown()
starter.forward(29 * len(color_list))
starter.penup()
starter.setposition(415, -82)
starter.pendown()
starter.forward(28 * len(color_list))
starter.penup()

y_pos = -70
for racer in color_list:
    color = racer
    racer = Turtle("turtle")
    racer.penup()
    racer.color(color)
    racer.goto(-420,y_pos)
    y_pos += 30
    racer_list.append(racer)
    racer.speed(0)      # 0=Fastest 1=Slowest

if bet:
    is_race_on = True
places = []
while is_race_on:
    for racer in racer_list:
        random_move = random.randint(1, 20)
        racer.forward(random_move)
        if racer.xcor() > 400:
            is_race_on = False
            places.append(racer.pencolor())
            starter.goto(0,0)
            starter.write(f"{places[0].capitalize()} wins!", align="center", font=("Arial", 12, "normal"))
            starter.goto(0,-30)
            if places[0].lower() == bet.lower():
                starter.write(f"You bet on {bet.capitalize()}, you win!", align="center", font=("Arial", 12, "normal"))
            else:
                starter.write(f"Unlucky, you bet on {bet.capitalize()}!", align="center", font=("Arial", 12, "normal"))

print(places)

screen.exitonclick()
