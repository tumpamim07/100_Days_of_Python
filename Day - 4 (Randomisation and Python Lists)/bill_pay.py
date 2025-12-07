#random person to pay the bill

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1 Option
print(random.choice(friends))

#2nd Option
random_friend = random.randint(0,4)
print(friends[random_friend])

#random color choose
colors = ["red", "blue", "green", "yellow", "purple"]
print(random.choice(colors))

color_index = random.randint(0,4)
print(colors[color_index])


#number
numbers = [10, 20, 30, 40, 50, 60]
print(random.choice(numbers))

number_list = random.randint(0,5)
print(f"Selected number is: {numbers[number_list]}")


#fruits
fruits = ["apple", "banana", "mango", "kiwi"]
print(random.choice(fruits))
print(random.choice(fruits))

select_fruit = random.randint(0,3)
print(fruits[select_fruit])
print(fruits[select_fruit])

#select friends
friends = ["Alice", "Bob", "Charlie", "David"]
print(f"Today i will call {random.choice(friends)}")

call_phone = random.randint(0,3)
print(f"Today i will call {friends[call_phone]}")


#task
tasks = ["study", "exercise", "cook", "read", "sleep"]  # List of tasks
choice_task = random.choice(tasks)                      # Pick a random task from the list
print(choice_task)
remove_task = tasks.remove(choice_task)                 # Remove the chosen task from the list (returns None)
print("Remaining tasks:", tasks)                        # Print the updated list after removal



#OPTION 2
tasks2 = ["study", "exercise", "cook", "read", "sleep"]  # List of tasks
choice_task2 = random.randint(0,4)
print(tasks2[choice_task2])
tasks2.pop(choice_task2)                    
print("Remaining Tasks:", tasks2)