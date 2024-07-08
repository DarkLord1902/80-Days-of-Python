import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type (0 for Rock), (1 for Paper), (2 for Scissors): "))
computer_choice = random.randint(0, 2)

if choice != int(choice):
    print("Oops! You have entered the invalid value, Please choose the number between 0-2: \n")
else:
    if choice > 2:
        print("Uh-oh! You have entered the invalid value, Try again and choose the number between 0-2 \n")
    elif choice == 0 or choice == 1 or choice == 2:
        if choice == 0:
            print(f"You chose Rock: \n{rock}")
        elif choice == 1:
            print(f"You chose Paper: \n{paper}")
        elif choice == 2:
            print(f"You chose Scissors: \n{scissors}")

        if computer_choice == 0:
            print(f"The Computer chose Rock: \n{rock}")
            if choice == 2:
                print("You Lose! Rock wins against scissors.")
            elif choice == 0:
                print("It's a Draw!")
            else:
                print("You Win!")

        if computer_choice == 1:
            print(f"The computer chose Paper: \n{paper}")
            if choice == 0:
                print("You lose! Paper wins against rock.")
            elif choice == 1:
                print("It's a Draw!")
            else:
                print("You Win!")

        if computer_choice == 2:
            print(f"The computer chose Scissors: \n{scissors}")
            if choice == 1:
                print("You lose! Scissors wins against Paper.")
            elif choice == 2:
                print("It's a Draw!")
            else:
                print("You Win!")