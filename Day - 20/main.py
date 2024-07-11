# Importing the turtle module
from turtle import Screen
# Importing snake which is created by own
from snake import Snake
# Importing food which is created by own
from food import Food
# Importing scoreboard which is created by own
from scoreboard import Scoreboard
# Importing time module
import time

# Create a screen
screen = Screen()
# set up the screen
screen.setup(width=600, height=600)
# Set up the background color
screen.bgcolor("black")
# Set up the title
screen.title("Snake Game")
# Off the auto animation
screen.tracer(0)

# assign the snake class to snake variable here
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Make the snake moves with keyboard keys assign the keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Make the condition for while loop
is_game_on = True
while is_game_on:
    # Update the screen
    screen.update()
    # assign the snake speed
    time.sleep(0.1)

    # Make to move the snake
    snake.move()

    # Make the conditions if snake eats the food then increase the scoreboard and extend the snake also refresh the
    # position of food
    if snake.head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        snake.extend()
        food.refresh()

    # Make the conditions to end the game whenever snake hit to the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # create a for loop to get the snake segments
    for segment in snake.segments[1:]:
        # Make the condition if snake hits to his own body or tail
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

# Make the game/program ends on click
screen.exitonclick()
