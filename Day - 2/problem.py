"""
Write a program that takes a two-digit number as input and outputs the sum of its digits.
Example: If input is 45 → Output should be 9 (4+5).
"""


two_digit_number = input()

first_digit = int(two_digit_number[0])  # convert the first character (index 0) to integer
second_digit = int(two_digit_number[1])  # convert the second character (index 1) to integer

print(first_digit + second_digit) 


#By using square brackets after a string, we can get a digit (character) from it