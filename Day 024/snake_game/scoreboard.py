from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # new
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    # day 24: new method to accommodate high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # new
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}") # converted int to string with f string

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()