from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball_game = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_upwards)
screen.onkey(key="Down", fun=r_paddle.move_downwards)
screen.onkey(key="w", fun=l_paddle.move_upwards)
screen.onkey(key="s", fun=l_paddle.move_downwards)




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball_game.move_speed)
    ball_game.move()

    #detects collision of ball with wall and bounce
    if ball_game.ycor() > 280 or ball_game.ycor() < -280:
        ball_game.bounce_y()

    #detects collision of ball with paddles
    if ball_game.distance(r_paddle) < 50 and ball_game.xcor() > 320 or ball_game.distance(l_paddle) < 50 and ball_game.xcor() < -320:
        ball_game.bounce_x()

    #detects rpaddle miss
    if ball_game.xcor() > 380:
        ball_game.reset_position()
        scoreboard.l_point()

    # detects lpaddle miss
    if ball_game.xcor() < -380:
        ball_game.reset_position()
        scoreboard.r_point()

screen.exitonclick()