"""
TODO - 1 - "- Use a while loop to let the user guess again.
            - The loop should only stop once the user has guessed all the letters in the chosen_word 
            - At that point display has no more blanks ("_"). Then you can tell the user they've won."            

"""
  
"""
TODO - 2 - "- Update the for loop so that previous guesses are added to the display string.
            - At the moment, when the user makes a new guess, the previous guess gets
              replaced by a "_". We need to fix that by updating the for loop. "            

"""

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct_word = []
game_over = False
while not game_over:
    guees_letter = input("Guess a Letter: ").lower()
    display = ""
    
    for letter in chosen_word:
        if letter == guees_letter:
            display += letter
            correct_word.append(guees_letter)
            
        elif letter in correct_word:
            display += letter
            correct_word.append(guees_letter)
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
