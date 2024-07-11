# Importing turtle module
from turtle import Turtle
# create a starting position of player
STARTING_POSITION = (0, -280)
# Create a turtle moving distance
MOVE_DISTANCE = 10
# Creating a finish line
FINISH_LINE = 280

# Create a class named as player with parameter Turtle
class Player(Turtle):

    # Define a __init__ method
    def __init__(self):
        super().__init__()
        # Set the head of turtle to upwards
        self.setheading(90)
        # set the shape of turtle
        self.shape("turtle")
        # set the color of the turtle
        self.color("black")
        # make a turtle to penup so it won't draw anything while moving
        self.penup()
        # Send turtle to starting position
        self.goto(STARTING_POSITION)

    # Define a method to move up
    def move_up(self):
        # Make a new y coordinate for turtle to move
        new_y = self.ycor() + MOVE_DISTANCE
        # Move the turtle
        self.goto(self.xcor(), new_y)

    # Define the method to bring turtle at starting position
    def starting_position(self):
        self.goto(STARTING_POSITION)