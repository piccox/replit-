# PyPassword Generator!

# letters = input("How many letters would you like in your password? \n") 
# syboles = input("How many symbols would you like? \n") 
# numbers = input("How many numbers would you like? \n")
# her is your password : 4fw*k8....

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Pypassword Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_number =int(input("How many numbers would you like? \n"))

#easy level : fghf*&23
password = " "
#nr_letters = 4 : range is to be 1 to 4 + 1 = 5
for char in range(nr_letters):
  #random_char = random.choice(letters)
  #password += random_char
  password += random.choice(letters)
  #print(random_char)
  print("password is", password, "char is", char)
print(f" print result ; {char}")

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
  print(password)
print(char)

for char in range(1, nr_number + 1):
  password += random.choice(numbers)
  print(password)
print(char)

print(password)



















 







