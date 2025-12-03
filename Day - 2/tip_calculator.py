"""
Write a program that works as a Tip Calculator.
The program should ask:
   1. What was the total bill?
   2. How much tip would you like to give? (10, 12, or 15)
   3. How many people to split the bill?
Then, it should calculate and print how much each person should pay.

"""



print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))

bill_will_tip = bill*(tip/100)
total_bill = bill + bill_will_tip
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
print(f"Each person should pay: ${final_bill}")


# :.2f means "fixed-point number with 2 decimals"