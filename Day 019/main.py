from turtle import Turtle, Screen
import random

is_race_on = False
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-100) + turtle_index * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # each turtle is 40 x 40 pixels, therefore 250 - (40/2) = 230
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner.")
            else:
                print(f"You lost. The {winning_colour} turtle is the winner.")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()