# Importing the turtle module
from turtle import Screen
# Importing paddle which is created by own
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# create a screen
screen = Screen()
# Set up the background color to the screen
screen.bgcolor("black")
# set up the screen size
screen.setup(width=800, height=600)
# Set up the screen title
screen.title("Pong")
# Turn off the auto-animation
screen.tracer(0)

# Set up the position of right paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))  # set up the left paddle
ball = Ball()
scoreboard = Scoreboard()

# Make a screen to listen events
screen.listen()
# Assign the keys for both right and left paddles to move up and down
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()