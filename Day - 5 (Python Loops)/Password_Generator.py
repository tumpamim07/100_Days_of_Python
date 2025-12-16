import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your passwords\n"))
nr_symbols = int(input(f"How many symbols would you like!\n"))
nr_number = int(input(f"How many numbers would you like!\n"))


#Easy Level
# password = ""

# for pass_char in range(0, nr_letters):
#     random_char = random.choice(letters)
#     password += random_char

# for pass_char in range(0, nr_number):
#     random_char = random.choice(numbers)
#     password += random_char

# for pass_char in range(0, nr_symbols):
#     random_char = random.choice(symbols)
#     password += random_char

# print(password)


#Hard Level
password_list = []                          # Empty list to store all selected characters
for char in range(0, nr_letters):           # Loop runs nr_letters times
    random_pass = random.choice(letters)    # Pick one random letter
    password_list.append(random_pass)       # Add it to the password list

for char in range(0, nr_number):
    random_pass = random.choice(numbers)
    password_list.append(random_pass)
for char in range(0, nr_symbols):
    random_pass = random.choice(symbols)
    password_list.append(random_pass)

# print(password_list)

# Shuffle the list to randomize character order
random.shuffle(password_list)
# print(password_list)

password = ""                         # Empty string to store final password


# Convert list characters into a single string
for char in password_list:            # Loop through each character in the list
    password += char                  # Add character to password string

# Display the final generated password
print(f"Your password is: {password}")