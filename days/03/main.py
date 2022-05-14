print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure - let's get started.")

direction = input("You're at a crossroad. Where do you want to go? Type 'right' or 'left'. ")

if direction == "right":
    action = input("After walking for some time, you hear a loud roar. Suddenly a lion shows up. What do you do? Type 'climb' to try to climb a nearby tree or 'run' to run as fast as possible. ")

    if action == "climb":
        print("You made it to the top of the tree, but the lion is not leaving. Guess you'll have to stay here for a while. Game Over :(")
    else:
        print("Oh no, that was a stupid idea, the lion is much quicker than you are and gets to you in no time. Game Over :(")
elif direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

    if action == "wait":
        door = input("You take the boat and arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

        if door == "red":
            print("Oh no, you enter a room full of fire. Game Over :(")
        elif door == "yellow":
            print("You see something sparkling in the back of the room. Its the treasure! You won!")
        elif door == "blue":
            print("Oh no, you enter a room of beasts! Game Over :(")
        else:
            print("You chose a door that doesn't exist. Game Over :(")
    else:
        print("Shortly after you get in the water, you get attacked by an angry crocodile. Game Over :(")
else:
    print("Oh no, you fell into a hole! Game Over :(")
