import random   # imports Python's random module so it can generate random numbers

# randint(a, b) gives a whole number between a and b (both included)
random_integer =  random.randint(1,10) 
print(random_integer)


# random() gives a float between 0.0 and 1.0
# multiplying by 10 makes it between 0.0 and 10.0
random_float_0_to_1 = random.random() * 10
print(random_float_0_to_1)


# uniform(a, b): random float between a and b (inclusive)
random_float = random.uniform (1,10)
print(random_float)

