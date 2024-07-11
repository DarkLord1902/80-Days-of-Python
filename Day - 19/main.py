# Importing turtle module
from turtle import Turtle, Screen
# Importing random module
import random

# Make a condition for game is on or off
is_race_on = False
# Make a screen
screen = Screen()
# Set up the height and width of screen
screen.setup(height=400, width=500)
# ask the user to bet
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which color turtle will win the race? Enter a color: ").lower()
# Make the color list
colors = ["red", "orange", "blue", "purple", "pink", "green"]
# assign the position of each turtle on start on y-axis
y_axis = [-100, -60, -20, 20, 60, 100]
# Make the empty list named as all_turtles
all_turtles = []

# make a for loop
for turtle_number in range(0, 6):
    # Make a new turtle
    new_turtle = Turtle(shape="turtle")
    # Make turtle to penup
    new_turtle.penup()
    # Assign the color to turtle from colors list
    new_turtle.color(colors[turtle_number])
    # Assign the starting position of every turtle
    new_turtle.goto(x=-230, y=y_axis[turtle_number])
    # Append all the turtles to the empty list created named as all_turtles
    all_turtles.append(new_turtle)

# Make the condition if the user bets on turtle then race is on
if user_bet:
    is_race_on = True

# Make while loop for race and turtles to move forward
while is_race_on:
    # Make the for loop
    for turtle in all_turtles:
        # Make condition to find the winning color of turtle
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            # Make the condition if the winning color is same as user bet then user is won.
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner.")
            # Break the while loop and end the race/program.
            is_race_on = False
        # Assign the random distance to move the every turtle in race
        random_distance = random.randint(0, 10)
        # make the turtle to move forwards
        turtle.forward(random_distance)

# Exit the game when click
screen.exitonclick()