from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10, 260)
        self.player_1 = 0
        self.player_2 = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"{self.player_1}  :  {self.player_2}", align="center", font=("courier", 18, "bold"))
        print(self.player_1, self.player_2)
