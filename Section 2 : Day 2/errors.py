# Error; str + int;  
# can only concatinate str to str (Not int) 
age = 32
#print("hello, I am " + age + " old.")



#Eorror correction: 
# 32 is int, this converts int to str 
a = (str(age))
print(a)
print(type(a))
print("hello, I am " + a + " old now.")

 
 




#mystrings and an interger; 
# e.g. 
meetup = 7 
mystring = "goodmorning"
mystring_1 = 'evening'
mystring_2 = "dinner"

print(meetup)
print(mystring)
print(mystring_1)
print(mystring_2)



# Not Error: can concatenate str + int
# by using f'string; 

print(f"hello {mystring} AI. shall we meet up at {meetup} this {mystring_1}? And let's have {mystring_2} together!")






 













# 






















