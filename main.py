from turtle import Turtle, Screen
from paddle import Paddle
import random

# Set up our screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
SCREEN_BACKGROUND_COLOR = "black"
SCREEN_TITLE = "Pong"
screen = Screen()
# Turn-off screen animation
screen.tracer(0)
screen.title(SCREEN_TITLE)
screen.screensize(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_BACKGROUND_COLOR)

game_on = True

# Draw our paddle to screen
paddle = Paddle()

# Listen for user input
screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

# Main loop
while game_on:

    screen.update()

screen.exitonclick()