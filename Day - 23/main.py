# Importing time module
import time
# importing turtle module
from turtle import Screen
# Importing player which is created by own
from player import Player
# Importing Car manager which is created by own
from car_manager import CarManager
# Importing the scoreboard
from scoreboard import Scoreboard

# creating a screen
screen = Screen()
# Set up the screen size
screen.setup(width=600, height=600)
# set up the title of the screen
screen.title("Turtle Crossing")
# Turn off the auto animation
screen.tracer(0)

# Call the player class
player = Player()
# call the scoreboard class
scoreboard = Scoreboard()
# Call the car manager class
car_manager = CarManager()

# Event handlers
screen.listen()
# Make the turtle move upwards when up key is pressed
screen.onkeypress(player.move_up, "Up")

# Creating a condition for while loop
game_is_on = True
# Make a while loop
while game_is_on:
    # Speed controls
    time.sleep(0.1)
    # Update the screen
    screen.update()

    # Add the car
    car_manager.add_car()
    # Move the car
    car_manager.move_car()

    # Creating a conditions
    if player.ycor() > 310:
        # Add the score point in scoreboard
        scoreboard.player_point()
        # Make the player move at starting position after ends of crossing
        player.starting_position()
        # Increase the speed after the first score
        car_manager.increase_speed()

    # Make a for loop to check if turtle hits to car
    for car in car_manager.cars:
        # Creating a condition if turtle hits to car
        if player.distance(car) < 20:
            game_is_on = False
            # Write the text game over on screen
            scoreboard.game_over()

# Make the program closed after click
screen.exitonclick()
