from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.ball_speed = speed
        self.x_direction = 1
        self.y_direction = 1

    def move(self):
        new_x = self.xcor() + (self.ball_speed * self.x_direction)
        new_y = self.ycor() + (self.ball_speed * self.y_direction)
        self.goto(new_x, new_y)





