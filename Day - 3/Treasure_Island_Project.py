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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Haunted Mansion. 👻💀")
print("Your mission is to find the treasure.")
choice1 = input("You're in front of the Haunted Mansion. " \
"Do you want to enter the mansion? " \
"Type 'Yes' or 'No'. 🏚️ ").lower()
if choice1 == "yes":
    print("Proceed inside")
    choice2 = input('You\'ve come to a hallway. ' \
    'Type "Left" or "Right" to choose a Hallway ').lower()
    if choice2 == "left":
        print("A Ghost Appears. ")
        choice3 = input('Type "Hide" or "Run" to choose an option ').lower()
        if choice3 == "run":
            print("Caught by a ghost! Game Over. 👻💀")
        elif choice3 == "hide":
            print("Found some items")
            choice4 = input("Pick an Item by choosing 'Key' or 'Candle'. 🗝️🕯️  ").lower()
            if choice4 == "key":
                print("You used the key. You escape. YOU WIN 🎉🎉")
            elif choice4 == "candle":
                print("Darkness surrounds you. Game Over 👻💀")    
            else:
                print("You typed a wrong option that doesn't exist. Game Over.")       
        else:
            print("You typed a wrong option that doesn't exist. Game Over. ❌❌")
    elif choice2 == "right": 
        print("Trapdoor Ahead. ⚠️⚠️ ")
        choice5 = input('Type "Jump" or "Avoid" to choose an option ').lower()
        if choice5 == "jump":
            print("You fall into a deep pit. Game Over 💥💥 ")
        elif choice5 == "avoid":
            print("You discovered a secret staircase leading underground. " \
            "Find hidden treasure " \
            "YOU WIN 🎉🎉")
        else:
            print("You typed a wrong option that doesn't exist. Game Over. ❌❌")
    else: 
        print("You typed a wrong option that doesn't exist. Game Over. ❌❌")
else:
    print("You left Safely. Game Over.🏃🏃")