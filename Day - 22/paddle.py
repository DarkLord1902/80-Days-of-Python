# Importing turtle module
from turtle import Turtle


# Create a class named as paddle with parameter of turtle
class Paddle(Turtle):

    # Define the __init__ method with parameter of position
    def __init__(self, position):
        super().__init__()
        # Make the shape of paddle
        self.shape("square")
        # Assign the color of paddle
        self.color("white")
        # Assign the paddle size
        self.shapesize(stretch_wid=5, stretch_len=1)
        # make the paddle to penup so it won't be drawn any line when it moves
        self.penup()
        # Make the paddle move to particular position
        self.goto(position)

    # define the method to move the paddle up
    def go_up(self):
        # make the new y coordinate
        new_y = self.ycor() + 20
        # Move the paddle to up
        self.goto(self.xcor(), new_y)

    # Define the method to move paddle down
    def go_down(self):
        # make the new y coordinate
        new_y = self.ycor() - 20
        # Move paddle to down
        self.goto(self.xcor(), new_y)