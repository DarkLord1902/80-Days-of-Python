# Importing the logo from art.py
from art import logo

# Defining the add function
def add(n1, n2):
    return n1 + n2

# defining the sub function
def sub(n1, n2):
    return n1 - n2

# defining the multiply function
def multiply(n1, n2):
    return n1 * n2

# defining the division function
def division(n1, n2):
    return n1 / n2

# creating a dictionary known as operations
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": division,
}

# Defining the function known as calculator
def calculator():
    # Print the logo
    print(logo)

    # Taking the input from user which is the first number.
    num1 = float(input("What is your first number?: "))
    # crating a condition for while loop
    run = True
    while run:
        # creating a for loop on operations
        for i in operations:
            print(i)
        # Take the math operation which have to perform by user as input
        perform = input("Type a math operation: ")
        # Take the next number from user
        num2 = float(input("What is the next number?: "))

        # the operations to perform assigning to calculation variable
        calculation = operations[perform]
        # assigning the answer to the answer variable after calculation
        answer = calculation(num1, num2)

        # printing the answer
        print(f"{num1} {perform} {num2} = {answer}")
        print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation." )
        # taking input for continue the calculation
        continue_calc = input("Type 'y'/'n'/'new': ").lower()
        # making if condition if user type y
        if continue_calc == "y":
            # the while loop will run again
            run = True
            # Just it will take previous answer as first number
            num1 = answer
        # If user types n
        elif continue_calc == "n":
            # The program will stop as it breaks the while loop
            run = False
            print("\n Goodbye!")
        # If user types new
        elif continue_calc == "new":
            # It will start the program newly from start
            calculator()
        # If user types something else
        else:
            print("Invalid response")
            # It will end the program
            run = False
            print("\n Goodbye!")
# Calling the calculator function
calculator()