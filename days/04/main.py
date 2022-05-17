# Rock, Paper, Scissors

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

options = [["Rock", "Paper", "Scissors"], [rock, paper, scissors]]

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_number > 2 or user_number < 0:
    print(f"{user_number} is not a valid option. You lose :(")
else:
    user_selection_string = options[0][user_number]

    computer_number = random.randint(0, len(options[1]) - 1)

    computer_selection_string = options[0][computer_number]

    print(f"You chose {user_selection_string}")
    print(options[1][user_number])

    print(f"Computer chose {computer_selection_string}")
    print(options[1][computer_number])

    if user_number == computer_number:
        print("It's a draw!")
    elif user_number == 0 and computer_number == 2:
        print("You win!")
    elif computer_number == 0 and user_number == 0:
        print("You lose :(")
    elif computer_number > user_number:
        print("You lose :(")
    elif user_number > computer_number:
        print("You win!")
