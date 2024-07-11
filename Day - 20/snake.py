# Importing turtle module
from turtle import Turtle

# Initialize the starting position of each segment of snake
# The format is [head, body, tail]
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# Assign for how much distance the snake is going to move
MOVE_DISTANCE = 20
# ASSigning angles of Snake
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Create a class known as snake
class Snake:

    # Define the __init__ method
    def __init__(self):
        # Create an empty list known as segments
        self.segments = []
        # Call the Create_snake function
        self.create_snake()
        # Assign the head for the segment
        self.head = self.segments[0]

    # Define the create_snake method
    def create_snake(self):
        # Create a for loop to create a snake
        for position in STARTING_POSITION:
            # Call the add_segment method with position parameter
            self.add_segment(position)

    # Define the method to add the segment with parameter known as position
    def add_segment(self, position):
        # create a segment and assign the shape
        new_segment = Turtle("circle")
        # Assign the color to the segment
        new_segment.color("white")
        # Make the turtle to penup so it doesn't draw
        new_segment.penup()
        # Make the segment to go to the positions
        new_segment.goto(position)
        # Add this segments to the empty list named as segments
        self.segments.append(new_segment)

    # Define the method to extend the snake when he eats the food
    def extend(self):
        # Add the segment to position
        self.add_segment(self.segments[-1].position())

    # Define the method to move the snake
    def move(self):
        # Create a for loop to move the snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Make a new x-coordinate
            new_x = self.segments[seg_num - 1].xcor()
            # make a new y-coordinate
            new_y = self.segments[seg_num - 1].ycor()
            # Move the segments to new x and y coordinates
            self.segments[seg_num].goto(new_x, new_y)
        # Make the snake head move forwards
        self.head.forward(MOVE_DISTANCE)

    # Define the method to move snake up
    def up(self):
        # Make the condition if snake is not moving down then it can move up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Define the method to move snake down
    def down(self):
        # Make the condition if snake is not moving up then it can move down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Define the method to move snake left
    def left(self):
        # make the condition if snake is not moving right then it can move left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Define the method to move snake right
    def right(self):
        # Make the condition if snake is not moving left then it can move to right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
