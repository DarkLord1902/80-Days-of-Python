# Importing tkinter module
from tkinter import *


# Create a function to convert miles into kilometers
def miles_to_km():
    # Find the calculated answer
    calc_num = float(num_miles.get()) * 1.609
    # Update the answer label with calculated answer
    answer_label.config(text=round(calc_num, 2))


# Make the window
window = Tk()
# Give title to window
window.title("Miles to Km")
# Set up the size of window
window.config(padx=20, pady=20)

# Make a label for miles
miles_label = Label(text="Miles", font="Arial")
# Set up the label place
miles_label.grid(column=2, row=0)
# Set up the label size
miles_label.config(padx=10, pady=10)

# Make Km label
km_label = Label(text="Km", font="Arial")
# Set up the label place
km_label.grid(column=2, row=1)
# Set up the label size
km_label.config(padx=10, pady=10)

# Make a label for equals
equal_label = Label(text="Equals", font="Arial")
# Set up the position of label
equal_label.grid(column=0, row=1)
# Set up the label size
equal_label.config(padx=10, pady=10)

# Make the label for answer
answer_label = Label(text="0", font="Arial")
# Set up the position for this label
answer_label.grid(column=1, row=1)
# Set up the label size
answer_label.config(padx=10, pady=10)

# Make an entry label
num_miles = Entry(width=10)
# Set up the position of entry label
num_miles.grid(column=1, row=0)

# Make a button for calculation
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Show up the window
window.mainloop()
