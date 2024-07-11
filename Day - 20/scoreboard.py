# Importing turtle module
from turtle import Turtle

# Make the alignment of scoreboard
ALIGNMENT = "center"
# Make the font, size, style of scoreboard
FONT = ('Times New Roman', 24, 'bold')


# Create a class known as Scoreboard with parameter as Turtle
class Scoreboard(Turtle):

    # Define the __init__ method
    def __init__(self):
        super().__init__()
        # Assign the initial score
        self.score = 0
        # Hide the turtle
        self.hideturtle()
        # Penup the turtle so it won't draw anything
        self.penup()
        # Assign the color to scoreboard
        self.color("white")
        # Assign the position of scoreboard
        self.goto(0, 260)

    # Define the method to start the scoreboard
    def start_scoreboard(self):
        # Write the score and style it
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Define the method to increase the scoreboard whenever snake eats the food
    def increase_scoreboard(self):
        # First clear the old score
        self.clear()
        # Increment the initial score with +1
        self.score += 1
        # Call the start_scoreboard method
        self.start_scoreboard()

    # Define the method to get Game over text when snake hit
    def game_over(self):
        # Text should be in default position
        self.goto(0, 0)
        # Write the game over text and style it
        self.write(arg="Game Over!", align=ALIGNMENT, font=FONT)
