# Bankers who will pay the bill 


import random

name_string = input("Given me everybody's names, seperated by a comma. \n")

names = name_string.split(", ") 
print(names)
print(len(names))


num_items = len(names)
random_choice = random.randint(0,num_items - 1)
print(random_choice)

person_who_will_pay = names[random_choice]
print(person_who_will_pay + " going to buy the meal today. ")






 

 










