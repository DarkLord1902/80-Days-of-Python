# Importing tkinter module
from tkinter import *
# Importing math module
import math

# Assigning Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# Assigning Font name
FONT_NAME = "Courier"
# Assigning the total work minutes
WORK_MIN = 25
# Assigning the short break minutes
SHORT_BREAK_MIN = 5
# Assigning the long break minutes
LONG_BREAK_MIN = 20
# Initial repetitions
reps = 0
# Initial timer
timer = None


# Define a function known as reset timer
def reset_timer():
    window.after_cancel(timer)
    # Update the timer again
    canvas.itemconfig(timer_text, text="00:00")
    # Update the title label
    title_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    # Update the check label
    check_label.config(text="")
    # Define the global variable
    global reps
    reps = 0


# Define the function to start the timer
def start_timer():
    # Define global variable
    global reps
    # Increment the reps by 1
    reps += 1

    # Finding all work sec, short break sec, and long break sec
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Making conditions
    if reps % 8 == 0:
        # Update the title label
        title_label.config(text="Break", fg=RED)
        # Starts the countdown
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # Update the title label
        title_label.config(text="Break", fg=PINK)
        # Starts the countdown
        count_down(short_break_sec)
    else:
        # Update the title label
        title_label.config(text="Work", fg=GREEN)
        # Starts the countdown
        count_down(work_sec)


# Define a function for countdown with count parameter
def count_down(count):
    # Find the count minute
    count_min = math.floor(count / 60)
    # Find the count seconds
    count_sec = count % 60
    # Making conditions
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Update the timer text
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # Define the global variable
        global timer
        # Make the countdown
        timer = window.after(1000, count_down, count - 1)
    else:
        # Call the start timer function
        start_timer()
        marks = ""
        # Creating a for loop when timer starts the check sign should have to be shown
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        # Update the check label
        check_label.config(text=marks)


# Create a window
window = Tk()
# Give a title to window
window.title("Pomodoro")
# Set up the size and background of window
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas for window and set up that canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Add the image to canvas
tomato_png = PhotoImage(file="tomato.png")
# Set up the size of image in canvas
canvas.create_image(100, 112, image=tomato_png)
# Create the timer text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# Set up the position of canvas
canvas.grid(column=1, row=1)

# Create a title label and set up that label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
# set up the position of title label
title_label.grid(column=1, row=0)

# Create a check label
check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
# Set up the position for check label
check_label.grid(column=1, row=3)

# Create a start button
start_button = Button(text="Start", command=start_timer)
# Set up the position for start button
start_button.grid(column=0, row=2)

# Create a reset button
reset_button = Button(text="Reset", command=reset_timer)
# Set up the position for reset button
reset_button.grid(column=2, row=2)

# display the window
window.mainloop()
