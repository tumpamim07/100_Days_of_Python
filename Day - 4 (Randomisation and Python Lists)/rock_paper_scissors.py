import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock,Paper,scissors]

if choose < 0 or choose >2:
    print ("You Typed and invalid number. You lose!")
    exit()
else:
    print(game_images[choose])

computer_chose = random.randint(0,2)
print(f"Computer Chose:")
print(game_images[computer_chose])


if choose == 0 and computer_chose == 2:
    print("You Win!")
elif choose == 0 and computer_chose == 1:
    print("You Lose!")
elif choose == 1 and computer_chose == 0:
    print("You Win!")
elif choose == 1 and computer_chose == 2:
    print("You Lose!")
elif choose == 2 and computer_chose == 1:
    print("You Win!")
elif choose == 2 and computer_chose == 0:
    print("You Lose!")
elif choose == computer_chose:
    print("It's a Draw!")
else: 
    print("You typed an invalid number. You lose!")