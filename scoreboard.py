from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.font = "courier", 40, "bold"
        self.goto(-100, 210)
        self.write(f"{self.player_1_score}", move=False, align='center', font=self.font)
        self.goto(100, 210)
        self.write(f"{self.player_2_score}", move=False, align='center', font=self.font)

    # If player scores a point, update points and update scoreboard
    def player_1_point(self):
        self.player_1_score += 1
        self.update_scoreboard()

    def player_2_point(self):
        self.player_2_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 210)
        self.write(f"{self.player_1_score}", move=False, align='center', font=self.font)
        self.goto(100, 210)
        self.write(f"{self.player_2_score}", move=False, align='center', font=self.font)