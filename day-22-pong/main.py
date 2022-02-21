from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
game_ball = Ball()
scorer = Scoreboard()

screen.listen()
# Move paddles
screen.onkey(key="Up", fun=right_paddle.move_up_r)
screen.onkey(key="Down", fun=right_paddle.move_down_r)
screen.onkey(key="w", fun=left_paddle.move_up_l)
screen.onkey(key="s", fun=left_paddle.move_down_l)

game_on = True
while game_on:
    screen.update()
    game_ball.move_ball()
    sleep(game_ball.move_speed)
    if game_ball.ycor() >= 280 or game_ball.ycor() <= -280:
        game_ball.bounce()

    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320:
        game_ball.hit_paddle()

    if game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.hit_paddle()

    if game_ball.xcor() > 380:
        scorer.player_1 += 1
        scorer.update_scores()
        game_ball.reset_position()

    if game_ball.xcor() < -380:
        scorer.player_2 += 1
        scorer.update_scores()
        game_ball.reset_position()

screen.exitonclick()
