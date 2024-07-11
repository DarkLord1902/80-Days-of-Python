# Importing the turtle module
from turtle import Turtle
# Importing random module
import random


# Create a class known as food with the parameter is Turtle
class Food(Turtle):

    # Define the __init__ method
    def __init__(self):
        super().__init__()
        # Assign the shape of food
        self.shape("circle")
        # Make the food penup so that it won't draw lines each time after it goes to new position
        self.penup()
        # Assign the size of food
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # assign the color of food
        self.color("red")
        # Assign the speed of food when it goes to new position
        self.speed("fastest")
        # refresh everytime when snake eats food so call the method refresh()
        self.refresh()

    # Define the refresh method
    def refresh(self):
        # make the random x and y position of food when everytime snake eats the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # Make the food to move to that position
        self.goto(random_x, random_y)
