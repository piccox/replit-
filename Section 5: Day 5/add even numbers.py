#Calculates the sum of all the Even numbers from 1 to 100. including 1 and 100

#print only statement in your console output; the final total

#using: for loop and if condition 
even_num = 0 
for s in range(1,101):
  if s % 2 == 0: 
    even_num += s
    #print(f" {s} is {even_num}")
  #print(f" even {s} is {even_num}")
print(f"Sum of the total is {even_num}")

 
   



print("------------ ----------\n using an other method: Step Size ") 
total_even_numbers = 0
for n in range(0,101,2): 
  total_even_numbers += n
print(f"the sum of total even number is {total_even_numbers}")