import random



import random  # Import the random module

print("""This is a dice roller script for D&D. You have several options.
From one to six. The following numbers correspond to the dice: 
D1 = 1D6 
D2 = 1D4
D3 = 1D8
D4 = 1D9
D5 = 1D10
D6 = 1D20
""")  # Print the options from one to six


user_option_dice_roll = input("What is your option from 1 to 6? or q to quit: ")
# Define random numbers for each dice option
D1 = random.randint(1, 6)   # Assigns a random number for 1D6
D2 = random.randint(1, 4)   # Assigns a random number for 1D4
D3 = random.randint(1, 8)   # Assigns a random number for 1D8
D4 = random.randint(1, 9)   # Assigns a random number for 1D9
D5 = random.randint(1, 10)  # Assigns a random number for 1D10
D6 = random.randint(1, 20)  # Assigns a random number for 1D20

def user_input(user_option_dice_roll):
    if user_option_dice_roll == "q":
        exit()  # Exit the program if user inputs "q"
    elif user_option_dice_roll == "D1":
        print(D1)
    elif user_option_dice_roll == "D2":
        print(D2)
    elif user_option_dice_roll == "D3":
        print(D3)
    elif user_option_dice_roll == "D4":
        print(D4)
    elif user_option_dice_roll == "D5":
        print(D5)
    elif user_option_dice_roll == "D6":
        print(D6)



user = user_input(user_option_dice_roll)

while True:
    user_option_dice_roll = input("What is your option from 1 to 6? or q to quit: ")
    user = user_input(user_option_dice_roll)
    print(user)

