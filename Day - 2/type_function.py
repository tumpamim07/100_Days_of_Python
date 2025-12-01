# Ask the user for their name and count how many characters it has
# num_char = len(input("What is your name?"))
# print(type(num_char))   # Shows the data type (it will be 'int')

# Convert the number of characters into a string
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")  # Concatenate (join) string with string


# Example of different data types conversion/casting in Python

a = 100
print(type(a))  
# Output: <class 'int'>
# Here, a is an integer (whole number)

print(type("Hello"))


b = str(100)
print(type(b))  
# Output: <class 'str'>
# Converted integer 100 into a string


c = float(123)
print(type(c))  
# Output: <class 'float'>
# Converted integer 123 into a floating-point number (decimal)


print(70 + float("100.75"))
# "100.75" is a string → converted to float → added with 70
# Output: 170.75


print(str(100) + str(25.5))
# Both numbers converted into strings → joined together
# Output: "10025.5" (not addition, just string concatenation)


print(type("32"))
print(type(32))
print(type(32.5))
print(type(True))

# print("Number of letters in your name: " + len(input("Enter Your name")))

name = input("Enter Your Name\n")
length_of_name = len(name)
print("Number of letters in your name: " + str(length_of_name))