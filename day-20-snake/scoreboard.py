from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("cyan")
        with open("data.txt") as highfile:
            self.high = highfile.read()
            if self.high == "":
                self.highscore = 0
            else:
                self.highscore = int(self.high)
        self.score = 0
        self.display_score()


    def display_score(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as high_file:
                high_file.write(f"{self.highscore}")
        self.score = 0
        self.display_score()

    def record_highscore(self):
        pass
