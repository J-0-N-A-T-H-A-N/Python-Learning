from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True

while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.display_score()
        snake.grow()


    # Detect collision with edges
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        sleep(2)
        score.reset_scoreboard()
        snake.reset_snake()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment.position()) < 10:
            sleep(2)
            score.reset_scoreboard()
            snake.reset_snake()



screen.exitonclick()
