# importing turtle module as t
import turtle as t
# Importing random module
import random

# Initializing the turtle
t.Turtle()

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

# choosing random color from list
random_color = (random.choice(color_list))
t.colormode(255)
t.penup()
t.speed("fastest")
t.hideturtle()

# Define the function for left and up
def left_up():
    # Setting up the heading
    t.setheading(90)
    # Move forward to turtle
    t.forward(50)
    # Again Set heading of turtle
    t.setheading(180)

# Creating a function known as right_up
def right_up():
    # Setting up the heading of turtle
    t.setheading(90)
    # Move turtle forward towards heading
    t.forward(50)
    # Again set heading for turtle
    t.setheading(0)

# Create a for loop
# Here first loop is for rows
for _ in range(5):
    # this for loop is for columns
    for _ in range(8):
        # setting up the dot size and color
        t.dot(20, (random.choice(color_list)))
        # Moving turtle to forward
        t.forward(50)
    # Call the left function
    left_up()
    for _ in range(8):
        # Moving turtle to forward
        t.forward(50)
        # setting up the dot size and color
        t.dot(20, (random.choice(color_list)))
    # Call the function
    right_up()

# appearing the screen
screen = t.Screen()
screen.exitonclick()