#find Second higest score in the list 
student_score = [98,79,98,97,96,98,90,91,80,83]

highest_score = 0 
second_high = 0
for i in student_score:
  print('--------',i,'---------')
  if i > highest_score: 
    second_high = highest_score
    highest_score = i 

    print(f"[if] i is {i},high score is {highest_score}, second is      {second_high}")
   

  elif second_high < i and highest_score> i:
    second_high = i 
    print('[elif] second high score -->', second_high)
    
  else: 
    print('[else] nothing happened for', i) 
print(highest_score,second_high)