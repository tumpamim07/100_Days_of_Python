"""
Write a program that works as a Tip Calculator.
The program should ask:
   1. What was the total bill?
   2. How much tip would you like to give? (10, 12, or 15)
   3. How many people to split the bill?
Then, it should calculate and print how much each person should pay.

"""



print("Welcome to the tip calculator!")

bill=float(input("What was the toatl bill? $"))  # total bill
tips = int(input("How much tip would you like to give? 10, 12, or 15?"))
split_bill = int(input("How many people to split the bill?"))

total_bill = bill + (bill * (tips / 100))
bill_per_person = round(total_bill / split_bill, 2)
bill_per_person = "{:.2f}".format(bill_per_person) # Format the result to always show 2 decimals (e.g. 27.50)
print(f"Each person should pay: ${bill_per_person}") 


# :.2f means "fixed-point number with 2 decimals"