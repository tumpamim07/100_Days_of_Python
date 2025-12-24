"""
TODO - 1 - "Create an empty String called placeholder.For each letter in the chosen_word, add a _ to placeholder. 
            So if the  chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess."
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
    


"""
TODO - 2 - "Create an empty string called "display". Loop through each letter in the chosen_word. If the letter at that position matches guess then 
            reveal that letter in the display at that position. 
            e.g. if the user guessed "p" and the chosen word was "apple", then display should be _ P P _ _. Print display and you should see the guessed letter in the correct position. 
            But every letter that is not a match is represented with a "_". "

"""

guess_letter = input("Guess a letter: ").lower()
print(guess_letter)

display = ""
for letter in chosen_word:
    if letter == guess_letter:
        display += letter
    else:
        display += "_"
print(display) 