from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -70, -40, -10, 20, 50]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} is the Winner!")
            else:
                print(f"You've won! The {winning_color} is the Winner!")
        ran = random.randint(0, 10)
        turtles.fd(ran)

screen.exitonclick()