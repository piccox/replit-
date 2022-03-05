#combining dictionary and functions 
#calculator 
'''
add
subtract
multiply
divide
'''
def add(num1, num2): 
  return num1 + num2 

def subtract (num1, num2):
  return num1 - num2 

def multiply (num1, num2):
  return num1 * num2 

def divide (num1, num2):
  return num1 / num2 


#storing these keys 
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


num_one = int(input("what is your first number? \n "))
#loop through this dictonary 
for symbol in operations: 
  print(symbol)
  
operation_symbol = input("Choose operation symbol the line above \n")
#to ask 
calculation_functions = operations[operation_symbol]
num_two = int(input("What is your second number?\n ")) 

answer = calculation_functions(num_one, num_two)  
print(f"{num_one} {operation_symbol} {num_two} = {answer} ")



'''
operation_list = [add,subtract, multiply, divide]
print(operation_list)

num_one = int(input("what is your first number?\n"))
choose_symbol = int(input("choose a list of operation symbole! \n"))
#print(choose_symbol)
calculation = operation_list[2]
num_two = int(input("what is your second num? \n"))


answer = calculation(num_one, num_two)
print(f"{num_one} {choose_symbol }{num_two} = {answer}")

'''