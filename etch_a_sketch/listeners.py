from turtle import Turtle, Screen
luc = Turtle()
screen = Screen()


def move_forwards():
    luc.fd(10)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()