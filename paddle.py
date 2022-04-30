from turtle import Turtle

# Paddle movement speeds
Y_SPEED = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        super().hideturtle()
        self.width = 20
        self.height = 100
        self.x_pos = 350
        self.y_pos = 0
        self.shape = "square"
        self.color = "white"
        self.speed = 20
        self.paddle = self.create_paddle()

    def create_paddle(self):
        # Create our paddle object
        paddle = Turtle()
        paddle.penup()
        paddle.color(self.color)
        paddle.shape(self.shape)
        # 20 pixels is default turtle size
        paddle.turtlesize(stretch_len=self.width / 20, stretch_wid=self.height / 20)
        # move into initial position
        paddle.setposition(self.x_pos, self.y_pos)
        return paddle

    def move_up(self):
        self.y_pos += Y_SPEED
        self.paddle.goto(self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos -= Y_SPEED
        self.paddle.goto(self.x_pos, self.y_pos)
