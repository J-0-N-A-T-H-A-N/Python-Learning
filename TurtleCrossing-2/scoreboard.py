from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.goto(-250, 260)
        self.clear()
        self.write(f"Level: {self.level}", font=("courier", 14, "bold"))

    def game_over(self):
        self.goto(-100, 30)
        self.write("G A M E   O V E R !", font=("courier", 18, "bold"))
