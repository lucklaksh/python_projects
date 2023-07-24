from turtle import Turtle, Screen

luc = Turtle()
screen = Screen()


def move_forwards():
    luc.fd(10)


def move_backwards():
    luc.fd(-10)


def clockwise():
    luc.right(10)


def counter_clockwise():
    luc.left(10)


def clear_screen():
    luc.home()
    luc.clear()



screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()