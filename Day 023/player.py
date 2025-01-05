from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.return_to_start_pos()


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def is_at_end_of_level(self):
        if self.ycor() > FINISH_LINE_Y:
            self.return_to_start_pos()
            return True
        else:
            return False


    def return_to_start_pos(self):
        self.goto(STARTING_POSITION)