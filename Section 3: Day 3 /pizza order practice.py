# order pizza : Large, Pep 
# size ; 
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25 

# Toppings; $ 
# pepperoni_small = 2
# pepperoni_large = 3
# extra_cheese = 1 
 

print("Welcome to Python Pizza Deliveries!")

size = input("what size pizza do you want? S, M, or L \n")
add_pepperani = input("do you want pepperani?  Y  or N \n") 
extra_cheese = input("do you want extra cheese? Y or N \n")

#create a variable
bill = 0 

if size == "S": 
  bill += 15
  #print(bill)
elif size == "M": 
  bill += 20
  #print(bill)
elif size == "L": 
  bill += 25
  #print(bill)

if add_pepperani == "Y": 
  if size == "S":
    bill += 2
    #print(bill)
  else:
    bill += 3
  
if extra_cheese == "Y": 
  bill += 1
else:
  pass 
print(f"your final bill is ${bill}")





 


 






