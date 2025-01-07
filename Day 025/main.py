import turtle
import pandas

FONT = ("Arial", 9, "normal")
image = "blank_states_img.gif"
guessed_states = []

screen = turtle.Screen()
screen.title("US States Game")

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

def display_state_on_map(user_answer):
    state_row = data[data.state == user_answer]
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    # .item() grabs the first element in the Panda Series, in our case we only have 1 value
    new_turtle.goto(state_row.x.item(), state_row.y.item())
    new_turtle.write(user_answer, align="center", font=FONT)
    guessed_states.append(new_turtle)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another State's name").title()

    if answer_state in states_list:
        display_state_on_map(answer_state)

screen.exitonclick()
