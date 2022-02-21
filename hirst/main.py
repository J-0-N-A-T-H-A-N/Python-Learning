import turtle as t
import random

my_colors = [
    (232, 227, 232), (211, 158, 211), (223, 238, 223), (217, 230, 217), (119, 170, 119), (237, 220, 237), (46, 107, 46),
    (181, 168, 181), (191, 143, 191), (227, 204, 227), (129, 181, 129), (146, 64, 146), (162, 82, 162), (46, 128, 46),
    (145, 26, 145), (197, 81, 197), (220, 85, 220), (62, 168, 62), (35, 169, 35), (224, 170, 224), (68, 28, 68),
    (149, 214, 149), (70, 33, 70), (30, 40, 30), (35, 55, 35), (236, 171, 236), (105, 118, 105), (143, 212, 143),
    (142, 31, 142), (14, 100, 14)
]
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()


def draw_grid(horizontal, vertical, gap, size):
    x_pos = 0 - int((horizontal * gap) / 2)
    y_pos = 0 - int((vertical * gap) / 2)
    for x in range(vertical):
        for _ in range(horizontal):
            color = random.choice(my_colors)
            tim.setposition(x_pos, y_pos)
            tim.dot(size, color)
            x_pos += gap
        x_pos = 0 - int((horizontal * gap) / 2)
        y_pos += gap


draw_grid(10, 10, 25, 15)

screen = t.Screen()
screen.exitonclick()
