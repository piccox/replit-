print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))

bill = 0

if height >= 120: 
  print("you can ride the rollercoaster!")

  age = int(input("what is your age? \n"))
  if age < 12:
    bill = 5
    print("child tickets are  $5")
  elif age <= 18:
    bill = 7
    print('youth tickets are $7')
  else: 
    bill = 12
    print("adult tickets are $12 ")
  
  wants_photo = input("Do you want a photo taken? Y or N \n")
  if wants_photo == "Y":
    #add $3 to their bill
    bill += 3
    print(bill)
    print(f"total ticket price {bill}")
 
else: 
  print("Sorry, you need to grow taller before you can ride!")

#print(f"total ticket price {bill}")
