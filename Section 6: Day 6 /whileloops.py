
""""
# while Loop: 
while something is true :
  do this 
  then do this 
  then do this 




# The functions move() and turn left 
#Hurdles race : 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump():
    move()
    turn_left() 
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
number_of_hurdles = 6 
while number_of_hurdles > 0: 
    jump()
    number_of_hurdles -= 1
    #6 - 1 becomes 5
    print(number_of_hurdles)
  





# The condition at_goal() & its all negation
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump():
    move()
    turn_left() 
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
  
while not at_goal(): 
    jump()


"""""