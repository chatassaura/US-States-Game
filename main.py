import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd


# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states_list = []
right_answers = []

def create_name(name, x, y):
    states = Turtle()
    states.penup()
    states.hideturtle()
    states.goto(x, y)
    states.write(name)


screen = Screen()
screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


while len(right_answers) < 50:
    states_list = pd.read_csv("50_states.csv")
    answer_state = (screen.textinput(title=f"{len(right_answers)} / {len(states_list['state'])} States", prompt="Whats Another State name?")).title()
    if answer_state == "Exit":
        # states to lean.csv and List Comprehension
        not_guess = [state for state in states_list['state'] if state not in right_answers]
        new_data = pandas.DataFrame(not_guess)
        new_data.to_csv("states to learn.csv")
        break

    for state in states_list['state']:
        if answer_state == state and answer_state not in right_answers:
            right_answers.append(answer_state)
            x = int(states_list[states_list['state'] == answer_state].x)
            y = int(states_list[states_list['state'] == answer_state].y)
            create_name(answer_state, x, y)
