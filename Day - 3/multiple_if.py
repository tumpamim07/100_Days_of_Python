"""
Write a Python program that decides whether a person is allowed to ride a rollercoaster and calculates their ticket price based on age and additional options.

Requirements:
Ask the user for their height in cm.
If the height is 120 cm or more, they are allowed to ride.
Otherwise, print:
"Sorry you have to grow taller before you can ride."
If they can ride, ask for their age and determine the ticket price:
Age 12 or below → ticket price = $5
Age 13-18 → ticket price = $7
Age 19 or above → ticket price = $12
Then ask if they want a photo:
If they type "y", add $3 to the total bill.
Finally, print their total bill in the format:
"Your final bill is $X"

"""

print("Welcome to the rolllercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    else: 
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")