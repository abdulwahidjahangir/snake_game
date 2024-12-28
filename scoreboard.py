from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", mode="r") as data:
            highscore = data.read()
            if highscore.strip() == '':
                self.high_score = 0
            else:
                self.high_score = int(highscore)

    def update_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
