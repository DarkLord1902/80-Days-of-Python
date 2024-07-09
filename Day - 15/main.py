MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

# Creating a function known as report
def report():
    # Printing the report of everything
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: $ {money['value']}")


# creating a function known as check_resources with the parameter of coffee_choice
def check_resources(coffee_choice):
    # create a variable that holds the true value to execute the function
    enough = True
    # Making the conditions
    if MENU[coffee_choice]['ingredients']['water'] > resources['water']:
        print(f"There isn't available water for a {coffee_choice}")
        enough = False
    if MENU[coffee_choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There isn't available coffee for a {coffee_choice}")
        enough = False
    if coffee_choice != "espresso":
        if MENU[coffee_choice]['ingredients']['milk'] > resources['milk']:
            print(f"There is isn't enough milk available for {coffee_choice}")
            enough = False
    return enough

# Defining the function known as process_coins which has the parameters quarter, dile, nickel, penny
def process_coins(quarter, dime, nickel, penny):
    # making the quarter
    quarter *= 0.25
    # making the dile
    dime *= 0.10
    # making the nickel
    nickel *= 0.05
    # making the penny
    penny *= 0.01
    # getting the total amount and store it in variable
    total = quarter + dime + nickel + penny
    # return the total
    return total

# Define the function known as deduct_resources with the parameter of coffee_choice
def deduct_resources(coffee_choices):
    # Deduct the resources on which coffee user chose and how much ingredients it takes to be made will get decremented.
    resources['water'] -= MENU[coffee_choices]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_choices]['ingredients']['coffee']
    if coffee_choices != "espresso":
        resources['milk'] -= MENU[coffee_choices]['ingredients']['milk']

# Defining the function known as coffee_machine
def coffee_machine():
    # making the condition for while loop
    is_on = True
    while is_on:
        # Take the input from user which coffee he wants
        choice = input("What would you like to have? Type 'espresso', 'latte', 'cappuccino': ").lower()
        # Taking the condition if user wants report
        if choice == "report":
            report()
            coffee_machine()
        # Taking the condition if user wants to off the coffee machine
        elif choice == "off":
            print("Turning off...")
            is_on = False
        # Taking conditions to make the coffee
        elif check_resources(choice):
            print("Please enter the coins: ")
            # Take the money
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many dimes?: "))
            pennies = int(input("How many pennies?: "))
            # Making conditions to give coffee
            if process_coins(quarters, dimes, nickels, pennies) == MENU[choice]['cost']:
                # Deduct the resources of what user wants
                deduct_resources(choice)
                # add money to value of coffee machine list
                money['value'] += MENU[choice]['cost']
                print(f"Here is your {choice} ☕. Have a Good One!")
            # making the condition if user gives more money in order to get change
            elif process_coins(quarters, dimes, nickels, pennies) > MENU[choice]['cost']:
                # Deduct the resources of what user wants
                deduct_resources(choice)
                # add money to value of coffee machine list
                money['value'] += MENU[choice]['cost']
                # minus the money of choice from user gave
                change = process_coins(quarters, dimes, nickels, pennies) - MENU[choice]['cost']
                # Round the money upto 2 decimal values
                change = round(change, 2)
                # Printing the change and choice
                print(f"Here is your $ {change} in change.")
                print(f"Here is your {choice} ☕. Have a Good One!")
            else:
                # Printing if user didn't gave enough money of what actual cost of choice
                print(f"Not enough Money!, $ {process_coins(quarters, dimes, nickels, pennies)} refunded.")

# calling the coffee machine function
coffee_machine()