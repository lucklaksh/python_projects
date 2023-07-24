from turtle import Turtle, Screen
import turtle as t

import random
# ----------------------square-------------------------
# luc = Turtle()
# luc.shape("turtle")
# luc.color("blue")
# for _ in range(4):
#     luc.forward(100)
#     luc.right(90)
#

#-------------dash-lines-------------
# luc = Turtle()
# luc.shape("turtle")
# luc.color("blue")
# for _ in range(50):
#     luc.forward(10)
#     luc.up()
#     luc.forward(10)
#     luc.down()

# -----------------polygons--------------
# luc = Turtle()
# luc.speed(0)
# list1 = [120, 90, 72, 60, 51.43, 45, 40, 36]
# i=0
# for l in list1:
#     for _ in range(3 + i):
#         luc.forward(100)
#         luc.right(l)
#     i += 1
#


#------------------random-walk--------------
# luc = Turtle()
# lis1 =[0, 90, 180, 270]
# colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange']
# luc.speed(0)
# luc.pensize(15)
# for _ in range(100):
#     luc.color(random.choice(colors))
#     luc.forward(20)
#     ch = random.choice(lis1)
#     luc.setheading(ch)
#

#

# luc = Turtle()
# t.colormode(255)
# lis1 =[0, 90, 180, 270]
# luc.hideturtle()
# def random_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color =(r,g,b)
#     return rand_color
#
# luc.speed(0)
# luc.pensize(15)
# for _ in range(100):
#     luc.color(random_colors())
#     luc.forward(20)
#     ch = random.choice(lis1)
#     luc.setheading(ch)
#
#

# ------------------------sphirograph-------------------------
luc = Turtle()
t.colormode(255)
luc.hideturtle()


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color =(r, g, b)
    return rand_color


ch = 0
luc.speed(0)
for _ in range(36):
    luc.color(random_colors())
    luc.circle(50)
    luc.setheading(ch)
    ch += 10









screen = Screen()
screen.exitonclick()