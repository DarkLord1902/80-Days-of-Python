# Importing logo
from art import logo
# creating a alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# defining a function named as caesar for encoding and decoding
def caesar(start_text, shift_amount, cipher_direction):
    # creating an empty string for final text
    end_text = ""
    # if user wants to decode it will decode the text
    if cipher_direction == "decode":
        shift_amount *= -1
    # Creating a for loop to get the characters from text that user puts
    for char in start_text:
        # Creating an if statement for if the characters are alphabet.
        if char.isalpha():
            # Get the position from alphabet as the index of that letter
            position = alphabet.index(char)
            # Store the position and shifting amount in a variable called as new_position
            new_position = position + shift_amount
            # adding new position alphabets to the end_text empty string
            end_text += alphabet[new_position]
        # creating else block if character is not alphabet just add it to the end_text
        else:
            end_text += char
    # printing the cipher text (encoded/decoded)
    print(f"Here's the {cipher_direction}d result: {end_text}\n")

# Making the condition for while loop to run repeatably
run = True
while run:
    # print the logo
    print(logo)
    # Take input if user wants to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Take the message from the user
    text = input("Type your message:\n").lower()
    # Take the shifting amount from user
    shift = int(input("Type the shift number:\n"))

    # If shift amount is more than 26 it will again start from 0 index which makes rotatable
    if shift > 26:
        shift = shift % shift == 0

    # calling the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    # Taking input from user if user wants to run this program again or not.
    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    # if user chose no it will end the program
    if choice == 'no':
        run = False
        print("Goodbye.")