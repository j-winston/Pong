from turtle import Turtle

# Paddle movement speed
Y_SPEED = 25


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.width = 20
        self.height = 100
        self.penup()
        self.color('white')
        self.shape('square')
        self.initial_position = starting_position
        self.speed = Y_SPEED
        self.turtlesize(stretch_len=self.width/20, stretch_wid=self.height/20)
        self.goto(self.initial_position)

    def move_up(self):
        new_y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), new_y_coordinate)

    def move_down(self):
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)

