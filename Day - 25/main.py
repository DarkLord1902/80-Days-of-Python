# Importing turtle Module
import turtle
# Importing pandas module
import pandas

# read the data from csv file
data = pandas.read_csv("India_States.csv")
# Make the screen
screen = turtle.Screen()
# Give title to the screen
screen.title("India States Game")
# Add the image of indian map to screen
image = "india_map.gif"
# Make the image visible on screen
screen.addshape(image)
# Make the turtle shape as image
turtle.shape(image)

# Create a turtle
t = turtle.Turtle()
# Hide the turtle
t.hideturtle()
# Penup the turtle so it won't draw anything
t.penup()

# Make a empty list of guessed states
guessed_states = []
# It will format the states names from list
states_list = data.state.to_list()

# Create a while loop to ask the user to guess the states
while len(guessed_states) < 29:
    answer = screen.textinput(title=f"{len(guessed_states)}/29 states guessed.", prompt="Name a State: ").title()

    # Create a condition to exit the game
    if answer == "exit":
        # Create a empty list known as missing_states
        missing_states = []
        # Create a for loop
        for state in states_list:
            # Make a condition to add the missing states in list
            if state not in guessed_states:
                missing_states.append(state)
        # Format the missing states list
        new_data = pandas.DataFrame(missing_states)
        # Convert the data into csv format
        new_data.to_csv("states_to_learn.csv")
        # Break the if statement
        break

        # Make the conditions if user guessed the state then it will appear on map
    if answer in states_list:
        if answer not in guessed_states:
            # Append the answer in guessed states
            guessed_states.append(answer)
            # Check the answer
            check_answer = data[data.state == answer].title()
            # It will check the lat and long
            x_axis, y_axis = int(check_answer.x), int(check_answer.y)
            # It will go to the state position
            t.goto(x_axis, y_axis)
            # It will write the answer
            t.write(f"{answer}")
