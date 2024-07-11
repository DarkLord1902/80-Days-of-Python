# Import the turtle module
from turtle import Turtle
# Import random module
import random

# make a list of colors of cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Assigning the starting move distance of car
STARTING_MOVE_DISTANCE = 5
# As far turtle scores the move distance is increasing means speed of car is increasing
MOVE_INCREMENT = 10

# Create a class known as Car manager
class CarManager:

    # Create a __init__ method
    def __init__(self):
        # Create a empty list for cars
        self.cars = []
        # Assigning the starting speed of cars
        self.starting_speed = STARTING_MOVE_DISTANCE
        # Assigning the speed of cars after the score increases
        self.increment = MOVE_INCREMENT

    # Create a method to add the car randomly
    def add_car(self):
        # Creating random chance of appearing a car
        car_chance = random.randint(1, 6)
        # Making condition if car chance == 6
        if car_chance == 6:
            # Create a new car
            new_car = Turtle("square")
            # make the car penup to don't draw anything while moving further
            new_car.penup()
            # Assigning random color to car
            new_car.color(random.choice(COLORS))
            # Assigning the size of car
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            # Assigning the random position of car
            random_y = random.randint(-250, 250)
            # Car comes from right hand side
            new_car.goto(300, random_y)
            # Append this new cars to empty list cars
            self.cars.append(new_car)

    # Define a method to increase the speed
    def increase_speed(self):
        # Incrementing the starting speed
        self.starting_speed += self.increment

    # Defining the method to move cars
    def move_car(self):
        # Making a for loop to move cars
        for car in self.cars:
            # Move th cars
            car.backward(self.starting_speed)