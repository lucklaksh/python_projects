import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's the name of another state?").title()
    if answer == "Exit":
        missed_states = []
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        new_state_dataframe = pandas.DataFrame(missed_states)
        new_state_dataframe.to_csv("states_to_learn")
        break

    if answer in states_list:
        t = turtle.Turtle()
        guessed_states.append(answer)
        t.hideturtle()
        t.penup()
        place = states[states.state == answer]
        t.goto(int(place.x), int(place.y))
        t.write(answer)
