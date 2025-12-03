print(int(8/3))          # Converts division result to int (truncates decimal part → 2)
print(round(8/3))        # Rounds result to nearest integer (2.67 → 3)
print(round(8/3, 2))     # Rounds result to 2 decimal places (2.67)
print(round(2.66666666, 2)) # Rounds 2.666... to 2 decimal places → 2.67


print(type(8//3))        # Floor division → gives integer (2), type is <class 'int'>
print(type(8/3))         # Normal division → gives float (2.666...), type is <class 'float'>

result = 4 / 2           # Normal division (result = 2.0, float type)
result /= 2              # result = result / 2 → 2.0 / 2 = 1.0
print(result)            # Prints 1.0


score = 0
# score = score + 1       # Traditional way to increment
score += 1               # Increases score by 1 (same as score = score + 1)
score -= 1               # Decreases score by 1
score *= 1               # Multiplies score by 1 (value stays same)
score /= 1               # Divides score by 1 (value stays same but converted to float)
print(score)             # Prints final score


# f-string
run_score = 0
height = 1.8
isWinning = True

print("Your score is " + str(run_score))  
# Concatenation: convert int to str manually before adding

print(f"your score is {run_score}, your height is {height}, you are winning is {isWinning}")  
# f-string: directly inserts variables inside {}


"""
f-string is to let you insert variables or expressions directly inside a string using {} without needing to convert them manually.
"""


