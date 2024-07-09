# Importing clear module from replit
from replit import clear
# Importing Random module
import random
# Importing Logo
from art import logo


# Defining the function called black jack game
def blackjack_game():
    # Defining the function known as start_deal
    def start_deal(cards):
        # Shuffle the cards using random
        shuffled = random.choice(cards)
        return shuffled

    # Defining the function if player lost the game
    def player_loss(player, cpu):
        # Creating if statement that if sum of the player is not = 21 and sum of the cpu = 21 then return true
        if sum(player) != 21 and sum(cpu) == 21:
            return True
        # Also if sum of player and cpu = 21 then too return true
        elif sum(player) == 21 and sum(cpu) == 21:
            return True

    # defining the function known as done playing
    def done_playing():
        # Getting the total sum of cards of player and computers
        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)
        # Printing the cards and sum of both player and computer
        print(f"Your hand is: {player_cards}, a total of {player_sum}.")
        print(f"The computer's hand is: {cpu_cards}, a total of {cpu_sum}.")
        # Creating conditions
        if sum(cpu_cards) > 21:
            print("The computer got bust, You Win!")
        elif player_loss(player_cards, cpu_cards):
            print("You Lose!")
        elif sum(player_cards) == 21 and sum(cpu_cards) != 21:
            print("You Win!")
        elif sum(player_cards) > 21:
            print("You got bust, You Lose!")
        elif player_sum == cpu_sum:
            print("It's a Draw!")
        elif player_sum > cpu_sum:
            print("You Win!")
        else:
            print("You Lose!")
        # Ask the user if you wanna play again or not?
        play_again = input("Do you wanna play again? Type 'y' or 'n': ").lower()
        # Making Conditions
        if play_again == "y":
            clear()
            blackjack_game()
        else:
            if play_again == "n":
                print("\n GoodBye!")

    # Defining the function to keep playing the game
    def keep_playing():
        # shuffled the cards and store to variable
        shuffled = start_deal(cards)
        # Appending the shuffled cards to player_cards
        player_cards.append(shuffled)
        # Appending the shuffle cards to cpu_cards
        cpu_cards.append(start_deal(cards))
        # Taking the sum of player_cards and cpu_cards
        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)

        # making a condition If there is 11 in player cards and player sum is >= 21
        if 11 in player_cards and player_sum >= 21:
            # Taking the index of 11 in player cards and store it into the variable known as ace
            ace = player_cards.index(11)
            # Assigning the player cards ace index to 1
            player_cards[ace] = 1
            # Taking the sum of player cards
            player_sum = sum(player_cards)
        print(f"Your hand is: {player_cards}, a total of {player_sum}.")
        print(f"The computer's hand is {cpu_cards}, a total of {cpu_sum}.")
        # Making the conditions
        if player_sum > 21:
            print("It's a bust, You Lose!")
            play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                clear()
                blackjack_game()
            elif play_again == "n":
                print("Thanks for playing GoodBye!")
        # If player sum is <= 21
        if player_sum <= 21:
            # ask the user for what's the choice for hit
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit == "y":
                keep_playing()
            elif hit == "n":
                done_playing()

    # print the logo
    print(logo)
    # Making the cards list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # creating an empty list known as player cards
    player_cards = []
    # creating an empty list known as cpu_cards
    cpu_cards = []
    # Appending cards to player cards
    player_cards.append(start_deal(cards))
    player_cards.append(start_deal(cards))
    # Appending cards to cpu_cards
    cpu_cards.append(start_deal(cards))
    # Printing player and computers first cards
    print(f"Your cards: {player_cards}")
    print(f"The computer's first card: {cpu_cards}")
    # Creating hit to get another card or pass
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == 'n':
        done_playing()
    elif hit == 'y':
        keep_playing()


blackjack_game()
