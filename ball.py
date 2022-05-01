from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.ball_speed = speed
        self.setheading(45)

    def move(self):
        self.forward(.02)
        # new_x = self.xcor() + self.ball_speed
        # new_y = self.ycor() + self.ball_speed
        # self.goto(new_x, new_y)

    def bounce(self):
        print("bounce")
        new_x = self.xcor() + self.ball_speed
        new_y = self.ycor() - self.ball_speed
        self.goto(new_x, new_y)


    def check_collision(self):
        # Check for collision with wall
        if self.distance(x=100, y=100) < 25:
            print("collision")
            return True
        return False





