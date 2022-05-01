from turtle import Turtle

# Paddle movement speed
Y_SPEED = 25


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.width = 20
        self.height = 100
        self.penup()
        self.color('white')
        self.shape('square')
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = Y_SPEED
        self.turtlesize(stretch_len=self.width/20, stretch_wid=self.height/20)
        self.goto(self.x_pos, self.y_pos)


    def move_up(self):
        self.y_pos += Y_SPEED
        self.goto(self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos -= Y_SPEED
        self.goto(self.x_pos, self.y_pos)
