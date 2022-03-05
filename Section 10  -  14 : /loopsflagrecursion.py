# Return vs Print 
# While loops, Flag and Recursion 

def add (a, b):
  return a + b 
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a,b):
  return a/b

operation = {"+": add, "-": subtract, "*": multiply, "/":divide}
first_number = int(input("what is your first number?"))

for symbole in operation: 
  print(symbole)

operation_system = input("what is your symbole above?")
second_number = int(input("what is your second number?"))

ans = 
  