from turtle import Screen
from game_char import GameChar
from car import Cars
from time import sleep
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = GameChar()
score = Score()
car_list = []
for _ in range(20):
    car = Cars()
    car_list.append(car)

screen.listen()
screen.onkey(key="Up", fun=timmy.move_up)
screen.onkey(key="Down", fun=timmy.move_down)

game_on = True
while game_on:
    sleep(car.carspeed)
    score.update_score()
    screen.update()
    for car in car_list:
        car.move_cars()

    #Detect finish line at top
    if timmy.ycor() >= 280:
        sleep(2)
        timmy.reset()
        car.carspeed *= 0.95
        score.level += 1

    #Detect collision
    for car in car_list:
        if car.distance(timmy) < 20:
            game_on = False
            score.game_over()


screen.exitonclick()
