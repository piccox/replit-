#how to break a Complex Problem down into a Flow Chart
"""
start Game
generate a random word
generate as many blanks as letters in word
ask the user to guess a letter
is the guessed letter in the word?
   - yes or 
   - no 
replace the blank with the letter 
lose a life
"""

#Step 1
word_list = ["ardvark", "baboon", "camel"]

#TODO 1 - randomly choose a word from the word_list and assign it to a variable called chosen_word
import random 
chosen_word = random.choice(word_list)

#Todo 2 - ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase 
guess = input("Guess a letter: ").lower()

#Todo 3 - check if the letter the user guessed (guess) is one of the letter in the chosen_word. 

for letter in chosen_word: 
  if letter == guess: 
    print("Right")
  else: 
    print("Wrong")
    