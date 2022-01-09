#replacing Blanks with Guesses 

word = ["ardvark", "baboon", "camel","apple"]
 
import random 
chosen_word = random.choice(word)
#testing code
print(f'Pssst,the solution is {chosen_word}')
# To do 1, create an empty list called a display
#e.g. letter in the chosen_word, add a "_" to 'display'
#so if the chosen_word was "apple", display should be ["_","_","_","_","-"] with 5 "_" representing each letter to guess. 
display = []
for _ in range(len(chosen_word)): 
  display += "_"
print('what comes next', display)

end_of_game = False
while not end_of_game: 
  guess = input("Guess a letter: ").lower()

  #Todo 2, loop through each position in the chosen_word:
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    print('check ---> ',letter)
    if letter == guess: 
      display[position] = letter 
      print("ola--->",display)
  print(display)

  if display == list(chosen_word) : 
    print("Hola! you got the word", chosen_word)
    end_of_game = True
    

print("End of Game!")
    

  
      