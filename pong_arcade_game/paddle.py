from turtle import Turtle
MOVE = 20

class Paddle(Turtle):
    def __init__(self, tuple_cors):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(tuple_cors)

    def move_upwards(self):
        y_cor = self.ycor() + MOVE
        self.goto(self.xcor(), y_cor)

    def move_downwards(self):
        y_cor = self.ycor() - MOVE
        self.goto(self.xcor(), y_cor)


