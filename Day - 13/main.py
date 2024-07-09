# Importing logos
from art import logo, vs
# Importing clear module from replit
from replit import clear
# Importing random module
import random
# Importing game Data
from game_data import data

# Defining the function known as profile
def profile():
    # choosing the random number between 0 - 49
    random_number = random.randint(0, 49)
    # Taking out the name from data of that random number index in dictionary
    name = data[random_number]["name"]
    # Taking out the follower count from data
    follower_count = data[random_number]["follower_count"]
    # taking out the description from data
    description = data[random_number]["description"]
    # Taking out the country from the data
    country = data[random_number]["country"]
    # putting all this data in format and store in variable
    compare = f"{name}, a {description}, from {country}."
    # return the compare and follower_count
    return compare, follower_count

# Define the function which is known as higher_lower
def higher_lower():
    # Taking two persons from profile function and stores them into variables
    profile_a, followers_a = profile()
    profile_b, followers_b = profile()
    # Making the conditions
    if followers_a == followers_b:
        profile_b, followers_b = profile()
    # making the initial score
    score = 0
    # Making the condition for while loop
    correct = True

    # Creating a while loop
    while correct:
        # clear the screen
        clear()
        # print the logo
        print(logo)
        # make the conditions
        if score > 0:
            print(f"Correct! Your current score is: {score}")
        # Compare the profiles
        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")

        # Taking input from user for his choice
        options = input("Who do you think has more following? Type 'a' or 'b': ").lower()
        # making conditions
        if options == "a" and followers_a >= followers_b:
            # Increment the score
            score += 1
            profile_b, followers_b = profile()
        elif options == "b" and followers_a <= followers_b:
            # Increment the score
            score += 1
            profile_a, followers_a = profile()
        elif options == "a" and followers_a < followers_b:
            print(f"\nIncorrect! Your final score is: {score}")
            # break the while loop and program will end
            correct = False
        elif options == "b" and followers_b < followers_a:
            print(f"\nIncorrect! Your final score is: {score}")
            # break the while loop and program will end
            correct = False

    # Ask the user if he wants to play again or not
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    # making the conditions
    if play_again == "y":
        higher_lower()
    elif play_again == "n":
        print("Thanks for playing!")

# calling the Function
higher_lower()