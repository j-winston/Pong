from turtle import Turtle, Screen
from paddle import Paddle
import random
from ball import Ball
import time
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


# Draw our two paddles to the screen
l_paddle = Paddle((-350, 200))
r_paddle = Paddle((350, 0))

# Draw our ball object and set speed
ball = Ball(speed=.01)

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
    if abs(ball.ycor() - 300) < 25:
        ball.y_direction *= -1
    if ball.ycor() + 300 < 25:
        ball.y_direction *= -1

    # If collision with left or right paddle, reverse direction of ball
    if abs(r_paddle.xcor() - ball.xcor()) < 25:
        ball.x_direction *= -1
    if abs(l_paddle.xcor() - ball.xcor()) < 25:
        ball.x_direction *= -1









screen.exitonclick()
