from turtle import Screen
from game_character import Player
from time import sleep
from cars import Car
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
cars = Car()
score = Score()

game_on = True
while game_on:
    sleep(cars.car_speed)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.car_list:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False

    # Player makes it to the other side
    if player.ycor() >= 280:
        sleep(2)
        player.reset_player()
        score.level += 1
        cars.car_speed *= 0.95
        score.update_score()

screen.exitonclick()
