import random

stages = ['''
      _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
    _|___
    ==========
''', ''' 
      _______
    |/      |
    |      (_)
    |      \|
    |       
    |    
    |
    _|___]
    ==========
    ''', '''
     _______
    |/      |
    |       _
    |       |
    |       |
    |      / 
    |
    _|___
    =========
    ''', ''' 
      _______
    |/      |
    |     
    |       |
    |       |
    |     
    |
    _|___
    =========
    ''','''
     _______
    |/      |
    |      
    |  
    |      
    |      
    |
    _|__
    =========
    ''']

end_of_game = False
mylist = ["ardv","babo","camel"]
chosen_list = random.choice(mylist)
word_length = len(chosen_list)

#todo1, create a variable called 'lives' to keep track of the number of lives left.
#set 'lives' to equal 6.
lives = 6
#testing code
print(f'the solution is {chosen_list}')

display = []
for _ in range(word_length): 
  display += "_"
print('display list --->',display)


while not end_of_game:
  guess = input("Guess a letter : ").lower()
#check guessed letter 
  for p in range(word_length): 
    letter = chosen_list[p]
    #print(f"current position: {p},current letter: {letter},current guess {guess}")

    if letter == guess: 
      display[p] = letter 
  print(stages[0])
#Todo2, if guess is not a letter in the chosen_list, then reduce 'lives' by 1. Again, if lives goes down to 0, and then the game should stop and it should print "You lose!"

  if guess not in chosen_list: 
    lives -= 1 
    if lives == 0: 
      end_of_game = True
      print("You lose!")

# join all the elements in the list and trun it into a string
  print(f"{' '.join(display)}")

#check if user has got all letters. 
  if "_" not in display: 
    end_of_game = True
    print("You win!")




