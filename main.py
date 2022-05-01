from turtle import Turtle, Screen
from paddle import Paddle
import random

# Set up our screen
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
l_paddle = Paddle(x_pos=-350, y_pos=200)
r_paddle = Paddle(x_pos=350, y_pos=0)

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


screen.exitonclick()
