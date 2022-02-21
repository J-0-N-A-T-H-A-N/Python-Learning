from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", font=("courier", 16, "bold"))

    def game_over(self):
        self.goto(-130, 20)
        self.write(f"G A M E  O V E R!", font=("courier", 20, "bold"))
