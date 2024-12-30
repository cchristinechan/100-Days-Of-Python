# import colorgram
#
# rgb_colours = []
# colours = colorgram.extract('image.jpg', 16)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import turtle
import random

# these colours were extracted and listed in terms of how frequent the colour appeared in the image
colour_list = [(171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155),
            (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (113, 131, 212), (184, 116, 161),
            (218, 92, 40)]

# requirements of the program
# paint a painting with 10 by 10 rows of spots
# each dot should be 20 in size and spaced by 50
screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

turtle.colormode(255)
tim.sety(-250)
for _ in range(10):
    tim.setx(-250)
    for _ in range(10):
        tim.dot(20, random.choice(colour_list))
        tim.fd(50)
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)

screen.exitonclick()
