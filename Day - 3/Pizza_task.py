
"""
Write a Python program that calculates the final bill for a pizza order based on user choices.

Requirements:
Ask the user what size pizza they want:
S = Small → $15
M = Medium → $20
L = Large → $25
Ask if they want pepperoni:
If Yes and size is S → add $2
If Yes and size is M or L → add $3
Ask if they want extra cheese:
If Yes → add $1
If the user types an invalid size, show:
"You typed the wrong inputs."
Then stop the program.
Print the final bill:
"Total bill will be $X"

"""

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1



elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill +=1
else:
    print("You typed the wrong inputs.")
    exit()
print(f"Total bill will be ${bill}")
