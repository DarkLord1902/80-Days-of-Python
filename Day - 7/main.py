# Importing clear from replit
from replit import clear
# Importing random module
import random
# Importing ascii arts
from hangman_words import word_list
from hangman_art import logo3, stages

# Create a variable to choose a random word
chosen_word = random.choice(word_list)
# Find the length of chosen word and store into a variable called word_length
word_length = len(chosen_word)

# To put the while loop defining the condition
end_of_game = False
# player has only 6 chances to guess the word
lives = 6

# Printing Hangman title logo
print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

# Creating an empty list called display
display = []
# creating a for loop to add the blank spaces "_" while guessing the word
for _ in range(word_length):
    display += "_"

# Put a while loop to repeat the game process for 6 chances
while not end_of_game:
    # Take a guess letter from user and store into the variable called guess
    guess = input("Guess a Letter: \n").lower()
    # Clear the screen
    clear()

    # creating condition if user already guessed a word and again guessing it
    if guess in display:
        print(f"You've already guessed {guess}.")

    # creating for loop getting that guess letter position in word
    for position in range(word_length):
        letter = chosen_word[position]

        # creating if condition for correct guessing
        if letter == guess:
            display[position] = letter

    # Creating if condition for guess word is not in chosen_word then one life is gone.
    if guess not in chosen_word:
        lives -= 1
        # creating nesting if condition for lives = 0 then it will end the game and man is hung.
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The Word is {chosen_word}.")

    print(f"{' '.join(display)}")

    # creating if condition to end the game and if user win there is no "_" in display.
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    # Printing the ascii art of hangman stages 
    print(stages[lives])