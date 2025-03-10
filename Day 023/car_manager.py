from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []


    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)


    def create_new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-250, 250)
            new_car.goto(300, y_pos)
            self.cars.append(new_car)


    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT