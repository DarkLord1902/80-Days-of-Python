# Importing logo
from art import logo
# Importing random
import random
# importing clear from replit
from replit import clear


# defining the function known as guess_the_number
def guess_the_number():
    # Choosing the random number between 1 - 100 and stores it into guess_this variable
    guess_this = random.randint(1, 100)
    print("Welcome to: ")
    print(logo)
    print(f"I am thinking a number between 1 and 100, try to guess it")
    # choosing the difficulty
    difficulty = input("choose the difficulty: Type 'easy' or 'hard': ").lower()
    # making the conditions
    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5

    # Creating a while loop
    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} guesses left for the number that I'm thinking of")
        else:
            print("Last try to guess the number that I'm thinking of")
        # Making the attempt to guess the number
        attempt = int(input("Take a guess: "))
        # making Conditions
        if attempt > guess_this:
            print("Too High!")
        elif attempt < guess_this:
            print("Too Low!")
        if guesses == 0:
            print("Game Over!")
        elif attempt == guess_this:
            # Defining the function known as game over
            def game_over():
                print(f"Correct! The answer was {guess_this}. Thanks for completing that! 😁")
                return guesses - guesses

            # Calling the game over function
            guesses = game_over()
        # decrementing the count of guesses
        guesses -= 1

    # Ask to user if they want to play again or not
    play_again = input("\n Do you want to play again? Type 'y' if yes and 'n' to quit: ").lower()
    # Making conditions
    if play_again == "y":
        clear()
        guess_the_number()
    else:
        print("GoodBye!")


# Calling the guess_the_number function
guess_the_number()
