# Extracting colors with colorgram package
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col = (r,g,b)
#     rgb_colors.append(col)
#
# print(rgb_colors)

import turtle as Turtle_module
from turtle import Screen
import random

Turtle_module.colormode(255)

rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197,
92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148,
129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


luc = Turtle_module.Turtle()
luc.penup()
luc.hideturtle()
luc.setheading(225)
luc.fd(300)
luc.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    luc.dot(20, random.choice(rgb_colors))
    luc.fd(50)
    if dots % 10 == 0:
        luc.setheading(90)
        luc.fd(50)
        luc.setheading(180)
        luc.fd(500)
        luc.setheading(0)

screen = Screen()
screen.exitonclick()