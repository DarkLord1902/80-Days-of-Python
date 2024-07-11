# Importing the turtle module
from turtle import Turtle
# making the alignment of scoreboard
ALIGNMENT = 'center'
# making the font style of scoreboard
FONT = ("Courier", 24, "normal")

# create a class known as Scoreboard with turtle parameter
class Scoreboard(Turtle):

    # Define the __init__ method
    def __init__(self):
        super().__init__()
        # Assigning the position of scoreboard
        self.goto(-290, 260)
        # Assigning color to scoreboard
        self.color("black")
        # MAke the scoreboard to penup so that it won't draw anything
        self.penup()
        # Hide the turtle
        self.hideturtle()
        # Assigning the initial score
        self.player_score = 0
        # calling the method known as update_scoreboard
        self.update_scoreboard()

    # define the method which is known as update scoreboard to update the scoreboard
    def update_scoreboard(self):
        # Clears the previous score on scoreboard
        self.clear()
        # Write the score on scoreboard
        self.write(f"Level:{self.player_score}", font=FONT)

    # Define the method to update the score and add point
    def player_point(self):
        # Increment the 1 point after completing each crossing
        self.player_score += 1
        # Update the scoreboard again
        self.update_scoreboard()

    # Define a method which is for game over
    def game_over(self):
        # If the game is over turtle will ring back to default position that is (0, 0)
        self.goto(0, 0)
        # Make the text comes in middle after the game is over
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
