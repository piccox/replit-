#coding exercise: Prime Number Checker 
#prime numbers 1 to 100 = 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 
#e.g. number = 7
'''
      7/2 = 
      7/3 =
      7/4 =
      7/5=
      
'''


def prime_check(number):
  is_prime = True

  for x in range(2, number):
    if number % x == 0:
      is_prime = False
      
  
  if is_prime: 
    print("it's a prime number.")
  else: 
    print("it's not a prime number.")

#call the function 
n = int(input("check this number: "))
prime_check(number=n)