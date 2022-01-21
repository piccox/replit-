# Dictionaries in Python ; Key & value

dict = {"Bug": "an error in a program that prevents the program from running as expected.", "Function": "a piece of code that you can easily CALL over and over again","Loop": "the acton of doing something over and over"}
print(dict,"\n")
print("----------------")


# Retriving items from dictionary: 
print(dict["Function"])


# Adding new items to dictionary ; 
dict["Loop"] = "the action of doing something"


#create an empty dictionary. the empty dict wipes an existing dictionary.
dict = {}
#print(dict)


#Edit an item in a dict; 
dict['Bug']='a moth in your computer.'

print("here is dict ", dict)




#Loop through a dictionary: 
for key in dict:
  print(f" Key --> {key},\n Value --> {dict[key]}\n")
  #print(f"value --> {dict[key]}\n")

























