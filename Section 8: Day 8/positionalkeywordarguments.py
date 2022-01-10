'''def greet_with_name(name): 
  #something = 123 
    # something --> paramenter 
    # 123 ---> argument
  print(f"there are {name}")

greet_with_name("John")

'''

# two perameters inside the function 
# Positional Arguments
'''''
def my_func(a,b,c):
  do this with ---> a 
  then do this with ---> b
  finally do this with ----> c 

'''''

def greet_with(name, location): 
  print(f"hello {name}")
  print(f"what is it like in {location}?")

#call this function 
greet_with("Diana","London")




# Functions with Keyword Arguments : 
def greet_with(name, location): 
  print(f"hello {name}")
  print(f"what is it like in {location}?")

#call this function 
greet_with(name="Diana",location="London")



