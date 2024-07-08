# Importing Clear from replit
from replit import clear
# Importing logo
from art import logo

# create a empty list which is called auction_info
auction_info = []


# Defining the function known as add_new_bidder to add the new bidder
def add_new_bidder(bidder_name, bidder_amount):
    # create a new empty dict known as new_bidder
    new_bidder = {}
    # make a two columns in dict known as bid and name
    new_bidder["bid"] = bidder_amount
    new_bidder["name"] = bidder_name
    # append all this new bidder info to auction_info list
    auction_info.append(new_bidder)


# create a auction condition for while loop
auction = True
while auction:
    # Print the logo
    print(logo)
    print("Welcome to the private bidding auction!")
    # taking name as input from user
    name = input("What is your name?: \n")
    # Taking bid amount from user
    bid = float(input("How much would you like to bid?: \n$ "))
    # Call the function
    add_new_bidder(bidder_name=name, bidder_amount=bid)

    # Asking to user if there is anymore bidders available for auction
    others = input("Are there any bidders for this auction? Type 'yes' or 'no'. \n")
    # If no other bidders then program will get out of the while loop
    if others == "no":
        auction = False
        # It makes highest bid = 0
        highest_bidder = 0
        # count is assigning to -1
        count = -1
        # creating a for loop on empty list auction_info
        for i in auction_info:
            # if condition to get highest bid amount
            if i["bid"] > highest_bidder:
                # it will assign bid amount to highest bidder
                highest_bidder = i["bid"]
                # Count will get incremented by 1
                count += 1
        # Winner will get who puts highest bid amount
        winner = auction_info[count]["name"]
        # print the winner and bid amount
        print(f"The highest bidder is {winner} with the bid of $ {highest_bidder}")
        print(f"Thank you for your participation.")
    else:
        # clear the screen
        clear()
