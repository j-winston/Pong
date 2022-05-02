from turtle import Turtle, Screen
from paddle import Paddle
import random
from ball import Ball
from scoreboard import Scoreboard
import time
from background import Background

# Set up our screen dimensions
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_BACKGROUND_COLOR = "black"
SCREEN_TITLE = "Pong"
screen = Screen()
# Turn-off screen animation
screen.tracer(0)
# Draw our screen
screen.title(SCREEN_TITLE)
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)

# Draw our scoreboards
scoreboard = Scoreboard()

# Draw our background
background = Background()

# Draw our two paddles to the screen
l_paddle = Paddle((-350, 200))
r_paddle = Paddle((350, 0))

# Draw our ball object and set speed
ball = Ball(speed=.01)

# draw background
background.draw_background()

# Listen for user input
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_on = True
# Main loop
while game_on:

    screen.update()

    ball.move()

    # Check for collision against walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_direction *= -1
        ball.ball_speed += .005

    # Check for collision with left or right paddle
    if abs(r_paddle.xcor() - ball.xcor()) < 20 and abs(r_paddle.ycor() - ball.ycor()) < 100:

        ball.x_direction *= -1
    if abs(l_paddle.xcor() - ball.xcor()) < 20 and abs(l_paddle.ycor() - ball.ycor()) < 100:
        ball.x_direction *= -1

    # Check if ball goes beyond right paddle
    if ball.xcor() > 405:
        scoreboard.player_1_point()
        ball.restart()

    # # Check if ball goes beyond left paddle
    if ball.xcor() < -405:
        scoreboard.player_2_point()
        ball.restart()









screen.exitonclick()
