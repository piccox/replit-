# Docstrings ; instead of using multiple comments, documentation of block of codes 
''''
def format_name(first_name, last_name): 
  if first_name == "" or last_name == "":
    return
    

  formated_first_name = first_name.title()
  formated_last_name = last_name.title()
  return f"{formated_first_name} {formated_last_name}" 

print(format_name(input("what is your first name?"),(input("What is your last name?"))))


'''


#Functions Quiz  

# Q - 1
'''
def add (n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

print(add(2,multiply(5,divide(8,4))))
'''


# Q - 2 
'''
def outer_function(a,b):
  def inner_function(c,d):
    return c + d
  return inner_function(a,b)

result = outer_function(5,10)
print(result)
'''


# Q - 3 
'''
def my_function(a):
  if a < 40:
    return
    print("terrible")
  elif a < 80:
    return "Pass"
  else:
    return "Great"
print(my_function(25))

'''