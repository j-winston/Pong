from turtle import Turtle


class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.style = 'bare'
        self.width(10)
        self.y_pos = 775
        self.x_pos = 0
        self.color("white")
        self.dimensions = (575, 775)
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=.5)
        self.draw_background()

    def draw_background(self):
        # Draw dashed line across court 30px in size
        dash_pos = 290
        for num in range(19):
            if num % 2 == 0:
                self.penup()
            else:
                self.pendown()
                self.goto(self.xcor(), self.ycor())
            dash_pos -= 30
            self.sety(dash_pos)
            self.hideturtle()







