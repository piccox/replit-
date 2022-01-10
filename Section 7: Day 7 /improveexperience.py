import random


#word_list = ["advert", "babilon", "hangman","livegame"]
from hangman_words import word_list
chosen_list = random.choice(handman_word.word_list)
word_length = len(chosen_list) 
print(f"the choice is :  {chosen_list}")

end_of_game = False 
lives = 7

display = []
for _ in range(word_length): 
  display += "_"
print('display list --',display)

while not end_of_game: 
  guess = input("Guess a letter: ").lower()
  for p in range(word_length):
    letter = chosen_list[p]
    
    if letter == guess: 
      display[p] = letter

  if guess not in chosen_list:
    lives -= 1
    if lives == 0: 
      end_of_game = True
      print("you lose!")
      
  print(f"{' '.join(display)}")

  if "_" not in display: 
    end_of_game = True
    print("you win!")
     
    

 