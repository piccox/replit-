# How to get the strength of a password in order to tackle that you would have to tackle it at the hard level..
# Hard Level requires to generate; g^2jk8&

import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Pypassword Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_number =int(input("How many numbers would you like? \n"))


password_list = []

for x in range(0, nr_letters+1): 
  password_list += random.choice(letters)
  #password_list.append(random.choice(letters))
  #print(password_list)
print(password_list, " ..random choice password")


for x in range (nr_symbols):
  password_list += random.choice(symbols)
  #print(password_list)
print(password_list, "using password with alphabets, symbols and numbers ")

for x in range(nr_number):
  password_list += random.choice(numbers)
  
  #print(f"{password_list} is the hard level password!")

print(f"{password_list} is the hard level password!")

random.shuffle(password_list,)
print(password_list,"Shuffle password!!!")


password = ""
for p in password_list:
  password += p 

print(f"Your final password is : {password}")
