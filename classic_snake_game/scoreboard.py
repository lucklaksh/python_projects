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
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}", move=False, align=ALIGN, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.print_score()
    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", move=False, align=ALIGN, font=FONT)

    def score_increase(self):
        self.score += 1
        self.print_score()
