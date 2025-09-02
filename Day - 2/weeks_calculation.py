#Write a program that tells the user how many years, weeks, and days they have left until age 90.

age = input("Enter your current age: ")     

years = 90 - int(age)                        # Calculate years left until 90
weeks = years * 52                           # Convert years into weeks (approx)
days = (90 * 365) - (int(age) * 365)         # Convert years into days (approx, ignoring leap years)

print(f"you have {years} years left.")       # Display years left
print(f"you have {weeks} weeks left.")       # Display weeks left
print(f"you have {days} days left.")         # Display days left
