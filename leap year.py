# A Leap Year! 
#on ever year is evenly divisible by 4
#excep every year that is evenly divisible by 100
#unless the year is also divisible by 400

year = int(input("which year do you want to check? "))


if year % 4 == 0:
  print("A Leap Year!")

  if year % 100 == 0: 
    if year % 400 == 0:
      print("Leap Year.")
  
    else:
      print("Not leap year.")
  else: 
    print("Leap Year.")
else: 
  print("Not Leap Year.")











