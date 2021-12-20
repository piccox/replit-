# playing a game;  Rock Paper Scissors 
import random 

rock = '''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
print(rock)




paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
print(paper)




scissors = '''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(scissors)



#list of hand guestures
game_images = [rock,paper,scissors]

user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number,you lose! ") 
else:
  print(game_images[user_choice])



#range; 0 = rock, 1 = paper, 2 = scissors
  computer_choice = random.randint(0,2)
  print("Computer chose")
  print(game_images[computer_choice])


# how to comepare to choose and win ; 
  if user_choice == 0 and computer_choice == 2:
    print("User wins!")
  elif computer_choice == 0 and user_choice == 2:
    print("Computer win!")

  elif computer_choice > user_choice: 
    #e.g. c == 0 and u == 2
    #e.g. c == 1 and u == 0
    #e.g. c == 2 and u == 1
    print("You lose!")
  elif computer_choice == user_choice:
    print("It's a draw")














