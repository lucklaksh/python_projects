from turtle import Turtle
FONT = ('courier', 20, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", move=False, align=ALIGN, font=FONT)

    def score_increase(self):
        self.score += 1
        self.print_score()
