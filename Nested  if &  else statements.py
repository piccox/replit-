#over 18 year old, then pay $18 but under 18yrs, pay $ 12

# < 12, pay $5, 
# 12 - 18 pay $7, 
# >18 pay $12 
eighteen_years_old = 12




# Nested  if & else 
# if condition: 
####nested block
#    if another condition:
#       do this
#.   elif another cond:
#.      do sth
#    else: 
#.      do this 
# else:
#    do this


print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))



if height >= 120: 
  print("you can ride the rollercoaster!")

  age = int(input("what is your age?"))
  if age < 12:
    print("you should pay $5")
  elif age > 12 and age < 18: 
    print('you should pay $7')
  else: 
    if age > 18: 
      print(f"you should pay ${eighteen_years_old}")
    else: 
      pass
  
else: 
  print("Sorry, you need to grow taller before you can ride!")






