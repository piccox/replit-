#replacing Blanks with Guesses 

word_list = ["ardvark", "baboon", "camel"]
 
import random 
chosen_word = random.choice(word_list)
#testing code
print(f'Pssst,the solution is {chosen_word}')
# To do 1, create an empty list called a display
#e.g. letter in the chosen_word, add a "_" to 'display'
#so if the chosen_word was "apple", display should be ["_","_","_","_","-"] with 5 "_" representing each letter to guess. 
display = []
for _ in range(len(chosen_word)): 
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#Todo 2, loop through each position in the chosen_word:
for i in range(len(chosen_word)):
  letter = chosen_word[i]
  if letter == guess: 
    display[i] = letter 
    #print(display)

print(display)

 
    